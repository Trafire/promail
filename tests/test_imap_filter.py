"""Tests for Imap Filter."""
import datetime

from promail.filters.imap_filter import ImapFilter


def test__get_date():
    """Test get date method."""
    f = ImapFilter(name="get_date")
    d = f._get_date("test_date", datetime.date(day=15, month=2, year=2022))
    assert d == ["test_date", "2022/02/15"]


def test__get_string():
    """Test get string method."""
    f = ImapFilter(name="get_string")
    assert f._get_string("get_string", "test") == ["get_string", "test"]


def test__join_tuple():
    """Test join tuple method."""
    f = ImapFilter(name="join_tuple")
    d = f._join_tuple("join_tuple", ("a", "b", "c"))
    assert d == [
        "OR",
        "OR",
        "OR",
        "join_tuple",
        "a",
        "join_tuple",
        "b",
        "join_tuple",
        "c",
    ]


#
# def test_bcc():
#     assert False
#
#
# def test_body():
#     assert False
#
#
# def test_cc():
#     assert False
#
#
# def test_sender():
#     assert False
#
#
# def test_sent_before():
#     assert False
#
#
# def test_size_larger():
#     assert False
#
#
# def test_subject():
#     assert False
#
#
# def test_to():
#     assert False
#
#
# def test_get_filter_list():
#     assert False
#
#
# def test_filter_results():
#     assert False
