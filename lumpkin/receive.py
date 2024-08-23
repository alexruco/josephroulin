#send.py

import imaplib
import email
from email.header import decode_header
import hashlib
from config import USERNAME, PASSWORD, IMAP_SERVER

def receive_emails(username, password, imap_server):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select("inbox")
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    emails = []

    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        subject_data = msg.get("Subject")
        if subject_data:
            decoded = decode_header(subject_data)
            if decoded:
                subject, encoding = decoded[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
            else:
                subject = "(No Subject)"
        else:
            subject = "(No Subject)"

        from_ = msg.get("From")
        to_ = msg.get("To")
        date = msg.get("Date")
        
        # Email body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if isinstance(payload, bytes):
                        body = payload.decode('utf-8')
                    else:
                        body = payload
        else:
            payload = msg.get_payload(decode=True)
            if isinstance(payload, bytes):
                body = payload.decode('utf-8')
            else:
                body = payload

        emails.append({
            "date": date,
            "from": from_,
            "to": to_,
            "subject": subject,
            "body": body
        })

    mail.close()
    mail.logout()

    email_hashes = encryptor(emails)

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
