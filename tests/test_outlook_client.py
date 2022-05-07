import time

from promail.clients.outlook import OutLookClient
from settings import TEST_EMAIL


def send_email():
    emailer = OutLookClient()
    text = "<h1>Test Email </h1>"
    emailer.send_email(TEST_EMAIL, "", "", "Test Email", text, "")
    time.sleep(3)


def test_outlook():
    try:
        send_email()
    except OSError:
        print("Test Skipped on non windows PC")
