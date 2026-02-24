# email_utils.py

import smtplib
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT


def send_mail(SUBJECT,BODY,TO_EMAIL=EMAIL_ADDRESS):
    """
    Send an email with a given subject and body.
    
    Parameters:
        subject (str): The email subject
        body (str): The email content (plain text)
        to_email (str): Recipient email (default is your own email)
    """
    
    try:
        # Create the message
        message = f"Subject: {SUBJECT}\n\n{BODY}"

        # Connect to the server and send
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)

        print(f"Email sent successfully to {TO_EMAIL}!")

    except Exception as e:
        print(f"Failed to send email: {e}")
    

    






 