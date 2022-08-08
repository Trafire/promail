"""Test Gmail Filters Class."""
from promail.filters.gmail_filter import GmailFilter


class TestGmailFilter:
    """Test Gmail Filter."""

    def test__validate(self):
        """Test Validate method."""
        client = GmailFilter("Test Filter")
        assert client._validate() is None

    def test__join_tuple(self):
        """Test Join tuple method."""
        client = GmailFilter("Test Filter")
        t = ("One", "Two")
        assert (
            client._join_tuple(term="test", data=t, seperator=" ") == "test:(One Two)"
        )

    def test_sender(self):
        """Test sender method."""
        client = GmailFilter("Test Filter", sender=("test@gmail.ca", "test2@gmail.ca"))
        assert client.sender == "from:test@gmail.ca OR from:test2@gmail.ca"

    # def test__get_boalean(self):
    #     assert False
    #
    # def test__get_string(self):
    #     assert False
    #
    # def test__get_date(self):
    #     assert False
    #
    # def test__get_toggle(self):
    #     assert False
    #

    #
    # def test_read(self):
    #     assert False
    #
    # def test_newer_than(self):
    #     assert False
    #
    # def test_not_sender(self):
    #     assert False
    #
    # def test_older_than(self):
    #     assert False
    #
    # def test_phrase(self):
    #     assert False
    #
    # def test_size(self):
    #     assert False
    #
    # def test_size_larger(self):
    #     assert False
    #
    # def test_size_smaller(self):
    #     assert False
    #
    # def test_sent_after(self):
    #     assert False
    #
    # def test_sent_before(self):
    #     assert False
    #
    # def test_starred(self):
    #     assert False
    #
    # def test_keyword(self):
    #     assert False
    #
    # def test_important(self):
    #     assert False
    #
    # def test_filename(self):
    #     assert False
    #
    # def test_category(self):
    #     assert False
    #
    # def test_bcc(self):
    #     assert False
    #
    # def test_around(self):
    #     assert False
    #
    # def test_attachment(self):
    #     assert False
    #
    # def test_label(self):
    #     assert False
    #
    # def test_folder(self):
    #     assert False
    #
    # def test_cc(self):
    #     assert False
    #
    # def test_to(self):
    #     assert False
    #
    # def test_subject(self):
    #     assert False
    #
    # def test_get_filter_string(self):
    #     assert False
    #
    # def test_filter_results(self):
    #     assert False
