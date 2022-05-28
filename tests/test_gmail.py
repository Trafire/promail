"""Tests for Gmail Client.

Requires Oauth credentials which are valid for a limited period,
therefore not suitable for CI/CD
"""

import pytest

from promail.clients.gmail import GmailClient
from promail.core.embedded_attachments import EmbeddedAttachments


@pytest.mark.e2e
def test_send_email() -> None:
    """Test Send email function."""
    client = GmailClient("promail.tests@gmail.com")
    image_1 = EmbeddedAttachments(r"assets\wolves-1341881.jpg")
    embedded = [image_1]
    client.send_email(
        "promail.tests@gmail.com",
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
            r"assets\1.pdf",
        ],
    )


@pytest.mark.e2e
def test_login() -> None:
    """Test Send email function."""
    client = GmailClient("promail.tests@gmail.com")
    assert client.service is not None


def test_gmail() -> None:
    """Temp test to allow testing suite to pass."""
    pass
