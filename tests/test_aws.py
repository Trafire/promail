import os

from promail.clients import AWSClient


class TestAWSClient:
    email = os.environ.get("GMAIL_TEST_EMAIL")
    region_name = os.environ.get("aws_region_name")
    aws_access_key_id  = os.environ.get("aws_access_key_id ")
    aws_secret_access_key = os.environ.get("aws_secret_access_key")
    client = AWSClient(email, region_name=region_name)
    def test__get_client(self):
        assert self.client._get_client("ses") is not None

    def test_aws_access_key_id(self):
        assert isinstance(self.client.aws_access_key_id, str)

    def test_aws_secret_access_key(self):
        assert isinstance(self.client.aws_secret_access_key, str)

    def test_verify_email(self):
        self.client.verify_email()

    def test_verify_domain(self):
        isinstance(self.client.verify_domain(),dict)

    def test_send_email(self):
        self.client.send_email(recipients=self.email,
                               subject="Promail Automated Test")
