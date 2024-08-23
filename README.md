# Lumpkin

Lumpkin is a simple Python package designed for handling emails via IMAP and SMTP. It allows users to receive and send emails programmatically, offering functionalities such as fetching emails from an inbox, generating hashes for email content, and sending emails with customized content.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Receiving Emails](#receiving-emails)
  - [Sending Emails](#sending-emails)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install Lumpkin, clone the repository and use `pip` to install the required dependencies.

```bash
git clone https://github.com/alexruco/lumpkin.git
cd lumpkin
pip install -r requirements.txt
```

## Configuration

Before using Lumpkin, you need to set up your email account details in the config.py file. Here's an example:


```python
# config.py

USERNAME = "your_email@example.com"
PASSWORD = "your_password"
IMAP_SERVER = "imap.yourdomain.com"
SMTP_SERVER = "smtp.yourdomain.com"
```
Replace the placeholders with your actual email credentials and server details.

## Usage
Receiving Emails

To fetch and process emails from your inbox, use the lumpkin_receive function from the receive.py module:

```python
from lumpkin.receive import lumpkin_receive

emails_with_hashes = receive_emails(USERNAME, PASSWORD, IMAP_SERVER)
for email_data in emails_with_hashes:
    print(f"Date: {email_data['email']['date']}")
    print(f"From: {email_data['email']['from']}")
    print(f"To: {email_data['email']['to']}")
    print(f"Subject: {email_data['email']['subject']}")
    print(f"Body: {email_data['email']['body']}")
    print(f"Hash: {email_data['hash']}\n")
```

This function connects to your email account, fetches all emails, and generates a hash for each email's content.
Sending Emails

To send an email, use the lumpkin_send function from the send.py module:

```python
from lumpkin.send import lumpkin_send

subject = 'Test Email'
body = 'This is a test email sent from Lumpkin.'
recipient = 'recipient@example.com'
sender_email = 'your_email@example.com'

send_email(SMTP_SERVER, 587, USERNAME, PASSWORD, subject, body, recipient, sender_email)

```

This function sends an email with the specified subject, body, and recipient details.

```
lumpkin/
│
├── lumpkin/
│   ├── __init__.py
│   ├── receive.py
│   ├── send.py
│
├── test/
│
├── .gitignore
├── config.py
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py

```
lumpkin/: Contains the core modules for receiving and sending emails.
test/: Directory for test scripts.
.gitignore: Specifies files and directories to be ignored by Git.
config.py: Configuration file for storing email credentials.
LICENSE: The project's license.
README.md: The file you're reading.
requirements.txt: Lists the Python dependencies for the project.
setup.py: Script for installing the package.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Make sure to include tests for any new features or bug fixes.
License

This project is licensed under the MIT License - see the LICENSE file for details.

The name of the project is a reference to William Lemuel "Willie" Lumpkin, a fictional supporting character appearing in American comic books published by Marvel Comics.