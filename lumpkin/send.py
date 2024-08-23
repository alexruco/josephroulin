#send.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import USERNAME, PASSWORD, SMTP_SERVER


def send_email(smtp_server, port, username, password, subject, body, recipient, sender_email):
    try:
        # Create a multipart message and set headers
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        # Add body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(username, password)  # Login to the email server

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)

        # Close the server connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Email configuration
smtp_server = SMTP_SERVER  # Replace with your SMTP server
port = 587  # Typically 587 for TLS, 465 for SSL
username = USERNAME
password = PASSWORD

# Email details
subject = 'Test Email'
body = 'This is a test email sent from Python.'
recipient = 'recip@email.com'
sender_email = 'send@email.com'

# Send the email
lumpkin_send(smtp_server, port, username, password, subject, body, recipient, sender_email)
