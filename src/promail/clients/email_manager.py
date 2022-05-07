import abc


class OutBoundManager(abc.ABC):
    def send_email(
        self, recipients: str, cc: str, bcc: str, subject: str, htmltext: str, plaintext
    ):
        pass


class InBoundManager(abc.ABC):
    def retrieve_last_items(self, max_items):
        pass
