"""Gmail Mail Client

# It is required that you set up an app password: https://security.google.com/settings/security/apppasswords

"""

from promail.clients.email_manager import OutBoundManager
import smtplib


class GmailClient(OutBoundManager):

    def __init__(self, account, password):
        self._account = account
        self._password = password

    def send_email(
            self: object,
            recipients: str,
            cc: str,
            bcc: str,
            subject: str,
            htmltext: str,
            plaintext: str,
    ) -> None:



        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(self._account, self._password)
        server.sendmail(self._account, recipients, htmltext)
        server.close()
        print('successfully sent the mail')



