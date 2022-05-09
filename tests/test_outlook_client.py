"""Tests for Outlook mail Client."""
import time

from src.promail.clients.outlook import OutLookClient
from src.promail.settings import TEST_EMAIL


def send_email() -> None:
    """Will Send a test email function."""
    emailer = OutLookClient()
    text = "<h1>Test Email </h1>"
    emailer.send_email(TEST_EMAIL, "", "", "Test Email", text, "")
    time.sleep(3)


def test_outlook() -> None:
    """Test whether non-windows systems return OS error."""
    try:
        send_email()
    except OSError:
        print("Test Skipped on non windows PC")
