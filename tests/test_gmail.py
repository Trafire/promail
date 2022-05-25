"""Tests for Gmail Client."""

from promail.clients.gmail import GmailClient
from promail.core.embedded_attachments import EmbeddedAttachments


def test_send_email() -> None:
    """Test Send email function."""
    client = GmailClient("promail.tests@gmail.com")
    image_1 = EmbeddedAttachments(
        r"C:\Users\Antoine\PycharmProjects\promail\wolves-1341881.jpg"
    )
    embedded = [image_1]
    client.send_email(
        "antoinewood@gmail.com",
        "",
        "",
        "Test email",
        f"""<h1>Test Email</h1>
        <img src="cid:{image_1}" />""",
        "Test Email ",
        embedded,
        [
            r"C:\Users\Antoine\PycharmProjects\promail\wolves-1341881.jpg",
            r"C:\Users\Antoine\PycharmProjects\promail\1.pdf",
        ],
    )


test_send_email()
