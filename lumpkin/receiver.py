import imaplib
import email
from email.header import decode_header

# Your account details
username = 'maggie@seomaggie.com'
password = '?@c%wN~6e7*~'
imap_server = 'mail.seomaggie.com'  # Often it is mail.yourdomain.com or imap.yourdomain.com

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

# Process the latest email
latest_email_id = email_ids[-1]

# Fetch the email by ID
status, msg_data = mail.fetch(latest_email_id, '(RFC822)')

# Extract the message content
msg = email.message_from_bytes(msg_data[0][1])

# Decode the email subject
subject, encoding = decode_header(msg["Subject"])[0]
if isinstance(subject, bytes):
    # If the subject is byte encoded, decode it
    subject = subject.decode(encoding if encoding else 'utf-8')

# From email address
from_ = msg.get("From")

print("Subject:", subject)
print("From:", from_)

# Close the connection and logout
mail.close()
mail.logout()
