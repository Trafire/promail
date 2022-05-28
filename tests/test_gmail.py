"""Tests for Gmail Client.

Requires Oauth credentials which are valid for a limited period,
therefore not suitable for CI/CD
"""
import os

from dotenv import load_dotenv  # type: ignore

import pytest

from promail.clients.gmail import GmailClient
from promail.core.embedded_attachments import EmbeddedAttachments


load_dotenv(".env")
GMAIL_TEST_EMAIL = os.environ.get("GMAIL_TEST_EMAIL", "")


@pytest.mark.e2e
def test_send_email() -> None:
    """Test Send email function."""
    client = GmailClient(GMAIL_TEST_EMAIL)
    image_1 = EmbeddedAttachments(r"tests/assets/wolves-1341881.jpg")
    embedded = [image_1]
    client.send_email(
        GMAIL_TEST_EMAIL,
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


@pytest.mark.e2e
def test_login() -> None:
    """Test Send email function."""
    client = GmailClient(GMAIL_TEST_EMAIL)
    assert client.service is not None
