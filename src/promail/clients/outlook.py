"""Mail Client for outlook."""
import sys

from src.promail.clients.email_manager import OutBoundManager
from src.promail.settings import DISPLAY, MAIL_ITEM

if sys.platform == "win32":
    import win32com.client as win32


class OutLookClient(OutBoundManager):
    """Client to instance of Outlook Running on local Windows Computer."""

    if sys.platform == "win32":
        outlook = win32.Dispatch("outlook.application")
        mail = outlook.CreateItem(MAIL_ITEM)

    preview = DISPLAY

    def __init__(self: object) -> None:
        """Return OS error on Initialization if platform is not windows."""
        if sys.platform != "win32":
            raise OSError("Outlook Client is only available on windows computers")

    def outbound(
        self: object,
        recipients: str,
        cc: str,
        bcc: str,
        subject: str,
        htmltext: str,
        plaintext: str,
    ) -> None:
        """Send Email email using Outlook client in windows.

        Args:
            recipients: semicolon seperated string of recipients will show in to section
                "Example Foo <bar@example.com>;Example2 Bar <foo@example.com"
            cc: semicolon seperated string of recipients will  be cc'd on email
                "Example Foo <bar@example.com>;Example2 Bar <foo@example.com"
            bcc: semicolon seperated string of recipients will be bcc'd on email
                "Example Foo <bar@example.com>;Example2 Bar <foo@example.com"
            subject: Subject of the email
            htmltext: An HTML string of text
            plaintext: A plain text alternative text
        """
        OutLookClient.mail.To = recipients
        OutLookClient.mail.Bcc = bcc
        OutLookClient.mail.Cc = cc
        OutLookClient.mail.Subject = subject
        OutLookClient.mail.HTMLBody = htmltext
        # EmailManager.mail.Body = plaintext

        if OutLookClient.preview:
            print("previewing", OutLookClient.preview)
            OutLookClient.mail.Display(True)
        else:
            OutLookClient.mail.Send()
