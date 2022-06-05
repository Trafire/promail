import email

from io import BytesIO
from email.message import EmailMessage


class Attachments:
    manager = email.contentmanager.raw_data_manager

    def __init__(self, email_attachment: EmailMessage):
        self.email_attachment = email_attachment

    @property
    def filename(self):
        return self.email_attachment.get_filename()

    def save_file(self, path):
        with open(path, "wb") as file:
            file.write(self.email_attachment.get_content(content_manager=self.manager))

    def get_data(self) -> BytesIO:
        obj = BytesIO()
        obj.write(self.email_attachment.get_content(content_manager=self.manager))
        obj.seek(0)
        return obj

    def __str__(self):
        return self.filename

    def __repr__(self):
        return f"Attachments({self.__str__()})"
