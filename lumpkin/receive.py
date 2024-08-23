#receive.py

import imaplib
import email
from email.header import decode_header
import hashlib
from config import USERNAME, PASSWORD, IMAP_SERVER

def receive_emails(username, password, imap_server):
    # Connect to the server
    mail = imaplib.IMAP4_SSL(imap_server)

    # Login to your account
    mail.login(username, password)

    # Select the mailbox you want to check
    mail.select("inbox")

    # Search for all emails
    status, messages = mail.search(None, 'ALL')

    # Convert messages to a list of email IDs
    email_ids = messages[0].split()

    emails = []

    # Process each email
    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(email_id, '(RFC822)')

        # Extract the message content
        msg = email.message_from_bytes(msg_data[0][1])

        # Decode the email subject
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        # From email address
        from_ = msg.get("From")
        
        # To email address (recipient)
        to_ = msg.get("To")

        # Date of the email
        date = msg.get("Date")

        # Email body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8')
        else:
            body = msg.get_payload(decode=True).decode('utf-8')

        emails.append({
            "date": date,
            "from": from_,
            "to": to_,
            "subject": subject,
            "body": body
        })

    # Close the connection and logout
    mail.close()
    mail.logout()

    # Call encryptor to generate hashes
    email_hashes = encryptor(emails)

    # Combine emails with their hashes
    emails_with_hashes = []
    for i in range(len(emails)):
        emails_with_hashes.append({
            "email": emails[i],
            "hash": email_hashes[i]
        })

    return emails_with_hashes

def encryptor(emails):
    email_hashes = []
    
    for email in emails:
        hash_object = hashlib.sha256()
        email_data = f"{email['date']}{email['from']}{email['to']}{email['subject']}{email['body']}"
        hash_object.update(email_data.encode('utf-8'))
        email_hashes.append(hash_object.hexdigest())
    
    return email_hashes

# Example usage
emails_with_hashes = lumpkin_receive(USERNAME, PASSWORD, IMAP_SERVER)
for i, email_data in enumerate(emails_with_hashes, 1):
    print(f"Email {i}:")
    print(f"Date: {email_data['email']['date']}")
    print(f"From: {email_data['email']['from']}")
    print(f"To: {email_data['email']['to']}")
    print(f"Subject: {email_data['email']['subject']}")
    print(f"Body: {email_data['email']['body']}")
    print(f"Hash: {email_data['hash']}\n")
