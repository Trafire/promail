from promail.clients.gmail import GmailClient
from promail.settings import TEST_EMAIL


def test_send_email():
    client = GmailClient(TEST_EMAIL, 'password')

    text = "<h1>Test Email </h1>"
    # client.send_email(TEST_EMAIL, "", "", "Test Email", text, "")
    pass


