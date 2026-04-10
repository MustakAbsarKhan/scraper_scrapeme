import aiohttp
import asyncio
from bs4 import BeautifulSoup as bs4
import pandas as pd
import random

baseURL = "https://scrapeme.live/shop/"

# Fetch HTML (Async)
async def fetch(session, url):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()
            print(f"Response Status Code: {response.status}")
            print(f"Fetched URL: {url}")
            return await response.text()
    except Exception as e:
        print(f"Error fetching the {url}: {e}")
        return None
    
    
# Parse HTML for products - Unchanged from the original scraper
def parse(html):
    soup = bs4(html, "lxml")
    products = soup.find_all("li", class_="product")
    
    products_info = []
    
    for product in products:
        titleTag = product.find("h2", class_="woocommerce-loop-product__title")
        priceTag = product.find("span", class_="woocommerce-Price-amount")
        imageTag = product.find("img", class_="attachment-woocommerce_thumbnail")
        urlTag = product.find("a", class_ = "woocommerce-LoopProduct-link")
        
        title = titleTag.text.strip() if titleTag else "No title"
        price = priceTag.text.strip() if priceTag else "No price"
        image = imageTag.get("src") if imageTag else "No image"
        url = urlTag.get("href") if urlTag else "No URL"
        
        products_info.append({
            "Title": title,
            "Price": price,
            "Image": image,
            "Url": url
        })
    
    return products_info

# Pagination - Get max page number
async def get_max_page(session):
    html = await fetch(session, baseURL)# Get the HTML of the first page to determine pagination
    if not html:
        return 1  # Default to 1 if we can't fetch the page
    
    soup = bs4(html, "lxml")
    
    pagination = soup.find("ul", class_="page-numbers")
    pagination_numbers = pagination.find_all("li") if pagination else []
    
    numbers = [int(li.text.strip()) for li in pagination_numbers if li.text.strip().isdigit()]
    
    max_page = max(numbers) if numbers else 1
    print(f"Max page number: {max_page}")
    
    return max_page

# Main async function to orchestrate the scraping
async def scrapeme_async(baseURL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        
        # Get total pages
        max_page_number = await get_max_page(session)
        
        # Build List of URLS
        urls = [
            baseURL if page == 1 else f"{baseURL}page/{page}/"
            for page in range(1, max_page_number + 1)
        ]
        
        # create tasks for fetching all pages concurrently
        tasks = [fetch(session, url) for url in urls]
        
        # Gather all HTML responses
        html_pages = await asyncio.gather(*tasks)
        
        # Parse all pages and collect product info
        all_products_info = []
        
        for html in html_pages:
            if html:
                all_products_info.extend(parse(html))
                
        print(f"Total products scraped: {len(all_products_info)}")
        return all_products_info

# Run the async scraper
if __name__ == "__main__":
    products = asyncio.run(scrapeme_async(baseURL))
    
    df = pd.DataFrame(products)
    df.to_csv("products_info_async.csv", index=False, encoding='utf-8-sig')
    
    print("Scraping completed. Data saved to products_info_async.csv")