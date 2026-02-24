# main.py

import time
from config import CHECK_INTERVAL,PRODUCT_URLS
from reports import daily_price_report
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    """
    Main loop that checks price every defined interval.
    """

    while True:
        try:
           
            logging.info("Checking product price...")

            daily_price_report(PRODUCT_URLS)
       
            logging.info("Waiting for next check...")

            #CHECK_INTERVAL=86400 seconds => runs the script every 24 hours
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"Error occurred: {e}")
            break   # stops the loop


if __name__ == "__main__":
    main()



