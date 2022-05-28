"""Tests EmbeddedAttachments."""
from promail.core.embedded_attachments import EmbeddedAttachments


def test_cid() -> None:
    """Test cid method."""
    image = EmbeddedAttachments(r"tests\assets\wolves-1341881.jpg")
    assert isinstance(image.cid, str)
    assert image.cid[0] == "<"


def test_read() -> None:
    """Test Read method."""
    image = EmbeddedAttachments(r"tests\assets\wolves-1341881.jpg")
    assert isinstance(image.read(), bytes)
