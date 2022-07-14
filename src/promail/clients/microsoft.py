"""Outlook/Hotmail Mail Client."""
from promail.clients.smtp_client import SmtpClient
from promail.clients.imap_client import ImapClient


class HotmailClient(SmtpClient, ImapClient):
    """Hotmail/Outlook.com Client."""

    def __init__(self, account, password, smtp_host="smtp-mail.outlook.com", imap_host="outlook.office365.com"):
        SmtpClient.__init__(self, account=account, password=password, host=smtp_host)
        ImapClient.__init__(self, account=account, password=password, host=imap_host)


