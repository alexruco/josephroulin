import pytest
from unittest.mock import patch, MagicMock
from josephroulin.receive import receive_emails

@patch('lumpkin.receive.imaplib.IMAP4_SSL')
def test_receive_emails(mock_imap):
    # Mocking the server connection and login
    mock_server = MagicMock()
    mock_imap.return_value = mock_server
    mock_server.login.return_value = 'OK', ['Logged in']

    # Mocking the email search and fetch
    mock_server.select.return_value = 'OK', [b'INBOX']
    mock_server.search.return_value = 'OK', [b'1 2']
    mock_server.fetch.side_effect = [
        ('OK', [(b'1 (RFC822 {3420}', b'Test email content 1')]),
        ('OK', [(b'2 (RFC822 {3420}', b'Test email content 2')]),
    ]

    # Mocking the email parsing
    with patch('email.message_from_bytes') as mock_msg:
        msg_instance = mock_msg.return_value
        msg_instance.get.return_value = 'test@example.com'
        msg_instance.is_multipart.return_value = False
        msg_instance.get_payload.return_value = 'Test email body'

        emails_with_hashes = receive_emails('username', 'password', 'imap.server.com')

        assert len(emails_with_hashes) == 2
        assert emails_with_hashes[0]['email']['from'] == 'test@example.com'
