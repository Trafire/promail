import base64

from email.policy import default

import email
from email.message import EmailMessage

from google.auth.transport.requests import Request  # type: ignore
from google.oauth2.credentials import Credentials  # type: ignore

from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore

from googleapiclient.discovery import build  # type: ignore
from googleapiclient.errors import HttpError  # type: ignore

from promail.core.attachements.attachments import Attachments


class Message:
    def __init__(self, msg):
        self.msg = email.message_from_bytes(
            base64.urlsafe_b64decode(msg["raw"]), _class=EmailMessage, policy=default
        )
        self._attachments = None

    @property
    def html_body(self):
        return self.msg.get_body(preferencelist=["html"])

    @property
    def plain_text(self):
        return self.msg.get_body(preferencelist=["plain"])

    @property
    def sender(self):
        return self.msg.get("from")

    @property
    def cc(self):
        return self.msg.get("cc")

    @property
    def bcc(self):
        return self.msg.get("bcc")

    @property
    def message_id(self):
        return self.msg.get("message-id")

    @property
    def to(self):
        return self.msg.get("to")

    @property
    def subject(self):
        return self.msg.get("subject")

    @property
    def date(self):
        return self.msg.get("date")

    @property
    def attachments(self):
        if self._attachments is None:
            self._attachments = {}
            for email_message_attachment in self.msg.iter_attachments():
                print(type(email_message_attachment))
                if email_message_attachment.is_attachment():
                    self._attachments[
                        email_message_attachment.get_filename()
                    ] = Attachments(email_message_attachment)
        return self._attachments

    def __str__(self):
        return self.subject
