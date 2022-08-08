"""AWSClient Test suite."""
# import os
#
# from promail.clients import AWSClient
#
#
# class TestAWSClient:
#     """AWS Client Tests."""
#
#     email = os.environ.get("GMAIL_TEST_EMAIL", "")
#     region_name = os.environ.get("aws_region_name")
#     aws_access_key_id = os.environ.get("aws_access_key_id ")
#     aws_secret_access_key = os.environ.get("aws_secret_access_key")
#     client = AWSClient(
#         email,
#         region_name=region_name,
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#     )
#
#     def test__get_client(self):
#         """Test Client method."""
#         assert self.client._get_client("ses") is not None
#
#     def test_aws_access_key_id(self):
#         """Test aws_access_key_id property."""
#         assert isinstance(self.client.aws_access_key_id, str)
#
#     def test_aws_secret_access_key(self):
#         """Test aws_secret_access_key property."""
#         assert isinstance(self.client.aws_secret_access_key, str)
#
#     def test_verify_email(self):
#         """Test verify_email method."""
#         self.client.verify_email()
#
#     def test_verify_domain(self):
#         """Test verify_domain method."""
#         isinstance(self.client.verify_domain(), dict)
#
#     def test_send_email(self):
#         """Test Sending Email."""
#         self.client.send_email(recipients=self.email, subject="Promail Automated Test")
