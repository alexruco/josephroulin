# josephroulin/send.py

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("email_sender.log"),
        logging.StreamHandler()
    ]
)

def send_email(smtp_server, port, username, password, subject, body, recipient, sender_email):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server using SSL for port 465
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            logging.info(f"Connecting to SMTP server {smtp_server} on port {port}...")
            print(f"Connecting to SMTP server {smtp_server} on port {port}...")
            
            server.login(username, password)
            logging.info("Logged in to SMTP server successfully.")
            print("Logged in to SMTP server successfully.")

            # Send the email
            server.sendmail(sender_email, recipient, msg.as_string())
            logging.info(f"Email sent successfully to {recipient}.")
            print(f"Email sent successfully to {recipient}.")

    except smtplib.SMTPAuthenticationError as e:
        logging.error("Authentication failed. Please check your username and password.")
        print("Authentication failed. Please check your username and password.")
        logging.error(f"Error details: {e}")
        print(f"Error details: {e}")
    except smtplib.SMTPConnectError as e:
        logging.error("Failed to connect to the SMTP server. Please check the server address and port.")
        print("Failed to connect to the SMTP server. Please check the server address and port.")
        logging.error(f"Error details: {e}")
        print(f"Error details: {e}")
    except smtplib.SMTPRecipientsRefused as e:
        logging.error("The recipient address was refused by the server.")
        print("The recipient address was refused by the server.")
        logging.error(f"Error details: {e}")
        print(f"Error details: {e}")
    except smtplib.SMTPException as e:
        logging.error("An SMTP error occurred.")
        print("An SMTP error occurred.")
        logging.error(f"Error details: {e}")
        print(f"Error details: {e}")
    except Exception as e:
        logging.error("An unexpected error occurred while sending the email.")
        print("An unexpected error occurred while sending the email.")
        logging.error(f"Error details: {e}")
        print(f"Error details: {e}")


