# scraper.py

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
from config import CSV_FILE_NAME,HEADERS
import os 
import re



def get_amazon_product_price(product_url):
    """
    -Fetch product title and price from Amazon page.
    -Send email if product price below threshold
    -Save data to CSV file.
    """

    # Send HTTP request
    try:
        page = requests.get(product_url, headers=HEADERS)
        page.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    # Parse HTML
    soup = BeautifulSoup(page.content, "html.parser")  

    # Get today's date
    today_date = datetime.date.today()

    # Extract product title
    title_element = soup.find(id="productTitle")
    if title_element:
        product_title = title_element.get_text(strip=True)
    else:
        product_title = "Title not found"
    
    # Extract product price
    price_element = soup.find("span", {"class": "a-offscreen"})
    if price_element:

        price_text = price_element.get_text(strip=True)
        
        # Extract currency (letters or symbol) and number from price text
        match = re.match(r"([A-Za-z$€£]+)?\s*([\d,\.]+)", price_text)
        if match:
            currency = match.group(1)  # 'EGP', 'GBP', '$', etc.
            price_str = match.group(2) # '8,353.66'
            numeric_price = float(price_str.replace(",", ""))

        # Save to CSV 
        save_to_csv(product_title,numeric_price,currency, today_date)

        return product_title,numeric_price,currency
                     
    else:
        # Save to CSV
        save_to_csv(product_title, "Price not found","n/a", today_date)
        return product_title,"Price not found","n/a"


  



def save_to_csv(title, price,currency, date):
    df = pd.DataFrame([[title, price,currency, date]], columns=['Title', 'Price','Currency', 'Date'])
    
    df.to_csv(CSV_FILE_NAME,
              mode='a',  # append
              header=not os.path.exists(CSV_FILE_NAME),  # only write header if file doesn't exist
              index=False)



