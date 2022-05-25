"""Package-wide test fixtures."""
from unittest.mock import Mock

from _pytest.config import Config
import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_email(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "account": "promail.tests@gmail.com",
        "to": "promail.tests@gmail.com",
        "text": "<h1>Test Email</h1>",
        "subject": "Test Subject"
    }
    return mock


def pytest_configure(config):
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")
