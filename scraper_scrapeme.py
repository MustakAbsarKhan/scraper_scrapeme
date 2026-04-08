"""
Simple web scraper for scrapeme.live
Extracts product titles and prices across all pages.
"""

import requests
from bs4 import BeautifulSoup as bs4
import time
import random

baseURL = "https://scrapeme.live/shop/"


def scrapeme(baseURL):
    # Create a session (faster and more consistent requests)
    session = requests.Session()

    # Add headers to look like a real browser
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    session.headers.update(headers)

    response = session.get(baseURL)
    print("Status:", response.status_code)

    # Get HTML and parse it
    html = response.text
    soup = bs4(html, "lxml")

    # Find pagination numbers (1,2,3,...)
    pagination_numbers = soup.find("ul", class_="page-numbers").find_all("li")

    # Extract only numeric page values
    list_of_numbers = []
    for number in pagination_numbers:
        number = number.text.strip()
        if number.isdigit():
            list_of_numbers.append(int(number))

    # Get the maximum page number
    max_page_number = max(list_of_numbers)
    print(f"Max page number: {max_page_number}")

    # Loop through all pages
    for page_number in range(1, max_page_number + 1):
        print(f"Scraping page {page_number}...")

        # Build correct URL for each page
        if page_number == 1:
            url = baseURL
        else:
            url = f"{baseURL}page/{page_number}/"

        # Send request
        response = session.get(url)
        print("Status:", response.status_code)

        html = response.text
        soup = bs4(html, "lxml")

        # Delay to avoid overwhelming server
        time.sleep(random.uniform(0.5, 2.0))

        # Find all products
        products = soup.find_all("li", class_="product")

        # Extract product info
        for product in products:
            # Get title safely
            titleTag = product.find("h2", class_="woocommerce-loop-product__title")
            title = titleTag.text if titleTag else "No title found"

            # Get price safely
            priceTag = product.find("span", class_="woocommerce-Price-amount")
            price = priceTag.text if priceTag else "No price found"

            # Print result
            print(f"Title: {title}, Price: {price}")


# Run the function
if __name__ == "__main__":
    scrapeme(baseURL)