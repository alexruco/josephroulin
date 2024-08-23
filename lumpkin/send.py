#send.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config import USERNAME, PASSWORD, SMTP_SERVER

def send_email(smtp_server, port, username, password, subject, body, recipient, sender_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)

        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)

        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
