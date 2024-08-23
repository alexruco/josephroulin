import pytest
from unittest.mock import patch, MagicMock
from lumpkin.send import send_email

@patch('lumpkin.send.smtplib.SMTP')
def test_send_email(mock_smtp):
    # Mocking the SMTP server connection and login
    mock_server = MagicMock()
    mock_smtp.return_value = mock_server
    mock_server.login.return_value = 'OK'

    # Call the function
    send_email('smtp.server.com', 587, 'username', 'password', 'Test Subject', 'Test Body', 'recipient@example.com', 'sender@example.com')

    # Check the sendmail call
    args, kwargs = mock_server.sendmail.call_args

    assert args[0] == 'sender@example.com'
    assert args[1] == 'recipient@example.com'
    assert 'Subject: Test Subject' in args[2]
    assert 'Test Body' in args[2]
