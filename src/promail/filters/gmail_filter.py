import re

from promail.filters.email_filter import EmailFilter
from typing import Optional
from datetime import datetime


class GmailFilter(EmailFilter):
    TIME_FRAMES = {
        "d": "Day",
        "m": "Month",
        "y": "Year",
    }

    def _validate(self) -> None:
        fields = "newer_than", "older_than"
        for field in fields:
            value = getattr(self, f"_{field}")
            if value is None:
                continue
            value = value.strip().lower()
            if len(value) < 2:
                raise IndexError(
                    f"{value} is not valid for{field} is expected to be either None "
                    f"or a string representing the number of a time period. "
                    f"example: 6d for 6 days. valid options are: {self.TIME_FRAMES}"
                )

            elif value[-1] not in self.TIME_FRAMES.keys():
                raise ValueError(
                    f"{value} is not valid for{field},"
                    f"string must end in one of the following values: {list(self.TIME_FRAMES.keys())} "
                )
            elif not value[:-1].isdigit():
                raise ValueError(
                    f"{value} is not valid for{field}, expecting value to begin with a number"
                )

    def join(self, term: str, data: Optional[tuple], seperator: str):
        if data is None:
            return ""
        if seperator == "OR":
            return " OR ".join([f"{term}:{d}" for d in data])
        elif seperator == " ":
            return f"{term}:(" + seperator.join([f"{d}" for d in data]) + ")"

    def get_boalean(self, term: str, value: tuple, data: Optional[bool]):
        if data is None:
            return ""

        elif data:
            return f"{term}:{value[1]}"

        else:
            return f"{term}:{value[2]}"

    def get_string(self, term: str, data: Optional[str]):
        if data is None:
            return ""
        return f"{term}:{data}"

    def get_date(self, term, date):
        if date is None:
            return ""
        return f"{term}:{date.strftime('%G/%m/%d')}"

    def get_toggle(self, term, data):
        if data:
            return f"{term}:{data}"
        return ""

    @property
    def sender(self):
        return self.join("from", self._sender, seperator="OR")

    @property
    def read(self):
        return self.get_boalean("read", ["read", "unread"], self._read)

    @property
    def newer_than(self):
        return self.get_string("newer_than", self._newer_than)

    @property
    def not_sender(self):
        return self.join("NOT from", self._not_sender, seperator="OR")

    @property
    def older_than(self):
        return self.get_string("older_than", self._older_than)

    @property
    def phrase(self):
        if self._phrase is None:
            return ""
        return self.join(
            "", tuple([f'"{phrase}"' for phrase in self._phrase]), seperator="AND"
        )

    @property
    def size(self):
        return "" if self._size is None else f"size:{self._size}"

    @property
    def size_larger(self):
        return self.get_string("larger", self._size_larger)

    @property
    def size_smaller(self):
        return self.get_string("larger", self._size_smaller)

    @property
    def sent_after(self):
        return self.get_date("after", self._sent_after)

    @property
    def sent_before(self):
        return self.get_date("before", self._sent_after)

    @property
    def starred(self):
        data = True if self._starred else None
        return self.get_toggle("starred", data)

    @property
    def keyword(self):
        if self._keyword is None:
            return ""
        else:
            return "(" + " ".join(self.keyword) + ")"

    @property
    def important(self):
        if self._important is None:
            return ""
        return self.get_toggle("is", "important")

    @property
    def filename(self):
        return self.join("filename", self._filename, "OR")

    @property
    def category(self):
        return self.get_string("category", self._category)

    @property
    def bcc(self):
        return self.join("bcc", self._bcc, "AND")

    @property
    def around(self):
        if self._around is None:
            return ""
        return (
            f"{self._around['first_term']}"
            "AROUND {self._around['apart']} "
            "{self._around['second_term']}"
        )

    @property
    def attachment(self):
        return self.get_toggle("has", "attachment" if self._attachment else None)

    @property
    def label(self):
        return self.get_string("label", self._label)

    @property
    def folder(self):
        return self.get_string("folder", self._folder)

    @property
    def cc(self):
        return self.join("cc", self._cc, "AND")

    @property
    def to(self):
        return self.join("to", self._to, "AND")

    def get_filter_string(self):
        return re.sub(
            " +",
            " ",
            " ".join(
                (
                    self.around,
                    self.attachment,
                    self.bcc,
                    self.category,
                    self.cc,
                    self.filename,
                    self.folder,
                    self.important,
                    self.keyword,
                    self.label,
                    self.newer_than,
                    self.not_sender,
                    self.older_than,
                    self.phrase,
                    self.read,
                    self.sender,
                    self.sent_after,
                    self.sent_before,
                    self.size,
                    self.size_larger,
                    self.size_smaller,
                    self.starred,
                    self.to,
                )
            ).strip(),
        )

    def filter_results(self, messages):
        """Removes messages in self.processed."""
        return filter(lambda msg: msg["id"] not in self.processed, messages)


# a = GmailFilter(
#     load_processed=True,
#     sender=("Antoinewood@gmail.com", "sue"),
#     older_than="99d",
#     sent_after=datetime.now(),
# )
#
# print(a.get_filter_string())
# # l = list(set(a.__dict__.keys()))
# # l.sort()
# # for value in l:
# #     print(
# #         f"self.{value.strip('_')}", end = ", "
# #     )
