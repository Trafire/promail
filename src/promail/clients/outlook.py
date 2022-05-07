from src.promail.clients.email_manager import OutBoundManager
import sys

from settings import MAIL_ITEM, DISPLAY


if sys.platform == "win32":
    import win32com.client as win32


class OutLookClient(OutBoundManager):
    """Client connection to instance of Outlook Running on local Windows Computer"""

    if sys.platform == "win32":
        outlook = win32.Dispatch("outlook.application")
        mail = outlook.CreateItem(MAIL_ITEM)
    preview = DISPLAY

    def __init__(self):
        if sys.platform != "win32":
            raise OSError("Outlook Client is only available on windows computers")

    def outbound(
        self, recipients: str, cc: str, bcc: str, subject: str, htmltext: str, plaintext
    ):
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
