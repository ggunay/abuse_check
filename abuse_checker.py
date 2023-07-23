import sys
import re
import requests
import whois
import socket
import smtplib
from email.mime.text import MIMEText

def get_abuse_contacts(domain):
    try:
        w = whois.whois(domain)
        # Check if 'emails' attribute is present and has data
        if hasattr(w, 'emails') and w.emails:
            return w.emails[:10]  # Fetch up to 10 email addresses
    except Exception as e:
        print(f"Error while fetching abuse contacts for {domain}: {e}")
    return []


def send_email(template, to_address, exchange, sender_email):
    try:
        msg = MIMEText(template)
        msg['Subject'] = 'Abuse Report'
        msg['From'] = sender_email
        msg['To'] = to_address

        # Connect to the Exchange server and send the email
        server = smtplib.SMTP(exchange)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_address}")
    except Exception as e:
        print(f"Error while sending email to {to_address}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python abuse_checker.py <IP/URL>")
        return

    target = sys.argv[1]

    # Read the environment variables from the config.env file
    email_template = os.environ.get('EMAIL_TEMPLATE')
    exchange_server = os.environ.get('EXCHANGE_SERVER')
    sender_email = os.environ.get('SENDER_EMAIL')
    abuse_contact_emails = get_abuse_contacts(target)

    for email in abuse_contact_emails:
        # Replace the placeholder in the email template with the IP or full URL
        filled_template = email_template.replace('<IP_OR_URL>', target)

        send_email(filled_template, email, exchange_server,sender_email)

if __name__ == "__main__":
    main()
