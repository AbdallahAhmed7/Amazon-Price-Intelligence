from scraper import get_amazon_product_price

from email_utils import send_mail


def daily_price_report(PRODUCT_URLS):
    """
    Collects all product prices for today and sends a summary email.
    """
    product_list = []  # This will store dictionaries with title and price

    for url in PRODUCT_URLS:    
        # get_amazon_product_price should return title and numeric_price
        result=get_amazon_product_price(url)
        if result:
            title,price,currency=result
            product_list.append({"title":title,"price":price,"currency":currency})

    # Build the email body
    report_body = "Daily Amazon Price Report:\n\n"
    for product in product_list:
        report_body += f"- {product['title']}: {product['price']} {product['currency']} \n"
    
    # Send email 
    send_mail("Daily Amazon Price Report", report_body)

