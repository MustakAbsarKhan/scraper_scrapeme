"""
Simple web scraper for scrapeme.live
Extracts product titles and prices across all pages.
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
import time
import random

baseURL = "https://scrapeme.live/shop/"


def scrapeme(baseURL):
    # Create a session (faster and more consistent requests)
    session = requests.Session()

    # Define headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    # Attach headers
    session.headers.update(headers)

    try:
        response = session.get(baseURL, timeout=10)
        response.raise_for_status()
        print(f"Response Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []

    # Parse HTML
    soup = bs4(response.text, "lxml")

    # Get pagination
    pagination = soup.find("ul", class_="page-numbers")
    pagination_numbers = pagination.find_all("li") if pagination else []

    list_of_numbers = []
    for number in pagination_numbers:
        text = number.text.strip()
        if text.isdigit():
            list_of_numbers.append(int(text))

    max_page_number = max(list_of_numbers) if list_of_numbers else 1
    print(f"Max page number: {max_page_number}")

    products_info = []

    # Loop pages
    for page_number in range(1, max_page_number + 1):
        print(f"\nScraping page {page_number}...")

        url = baseURL if page_number == 1 else f"{baseURL}page/{page_number}/"

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error on page {page_number}: {e}")
            continue

        soup = bs4(response.text, "lxml")

        time.sleep(random.uniform(0.5, 2.0))

        products = soup.find_all("li", class_="product")

        for product in products:
            titleTag = product.find("h2", class_="woocommerce-loop-product__title")
            priceTag = product.find("span", class_="woocommerce-Price-amount")
            imageTag = product.find("img", class_="attachment-woocommerce_thumbnail")
            urlTag = product.find("a", class_ = "woocommerce-LoopProduct-link")

            title = titleTag.text.strip() if titleTag else "No title"
            price = priceTag.text.strip() if priceTag else "No price"
            image = imageTag.get("src") if imageTag else "No image"
            url = urlTag.get("href") if urlTag else "No URL"

            data = {
                "Title": title,
                "Price": price,
                "Image URL": image,
                "Product URL": url
            }

            products_info.append(data)

            print(f"Title: {title}, Price: {price}, Image URL: {image}, Product URL: {url}")

    print(f"\nTotal products scraped: {len(products_info)}")
    return products_info


# Entry point
if __name__ == "__main__":
    data = scrapeme(baseURL)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save CSV
    df.to_csv("products_info.csv", index=False, encoding='utf-8-sig')

    print("\nCSV saved successfully!")