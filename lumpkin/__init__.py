# __init__.py
from .receive import receive_emails
from .send import send_email

__all__ = ["receive_emails", "send_email"]

def main():
    print("Lumpkin is running!")
