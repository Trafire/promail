"""Tests for SMTP Client."""
import os

from dotenv import load_dotenv  # type: ignore

from promail.clients.microsoft import HotmailClient
from promail.core.embedded_attachments import EmbeddedAttachments


def test_send_email() -> None:
    """Test Send email function."""
    account = HOTMAIL_TEST_EMAIL
    password = HOTMAIL_TEST_PASSWORD

    host = "smtp.office365.com"
    port = 587
    client = HotmailClient(account, password, host, port)
    image_1 = EmbeddedAttachments(r"tests/assets/wolves-1341881.jpg")
    embedded = [image_1]
    client.send_email(
        "protesting2022@outlook.com",
        "",
        "",
        "Test email",
        f"""<h1>Test Email</h1>
            <img width=20% src="cid:{image_1}" />
             <img width=20% src="cid:{image_1}" />
              <img width=20% src="cid:{image_1}" />
            """,
        "Test Email ",
        embedded,
        [
            r"tests/assets/1.pdf",
        ],
    )


load_dotenv(".env")
HOTMAIL_TEST_EMAIL = os.environ.get("HOTMAIL_TEST_EMAIL", "")
HOTMAIL_TEST_PASSWORD = os.environ.get("HOTMAIL_TEST_PASSWORD", "")
