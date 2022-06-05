import abc
import os.path
import pickle
from typing import Optional
import hashlib
from datetime import datetime


class EmailFilter(abc.ABC):
    def __init__(
        self,
        name: str,
        run_completed=False,
        around: Optional[dict] = None,
        attachment: Optional[bool] = None,
        bcc: Optional[tuple] = None,
        category: Optional[str] = None,
        cc: Optional[tuple] = None,
        filename: Optional[tuple] = None,
        folder: Optional[tuple] = None,
        important: Optional[bool] = None,
        label: Optional[tuple] = None,
        keyword: Optional[tuple] = None,
        newer_than: Optional[str] = None,
        not_sender: Optional[tuple] = None,
        older_than: Optional[str] = None,
        phrase: Optional[tuple] = None,
        sender: Optional[tuple] = None,
        size: Optional[int] = None,
        size_larger: Optional[str] = None,
        size_smaller: Optional[str] = None,
        sent_after: Optional[datetime] = None,
        sent_before: Optional[datetime] = None,
        starred: Optional[bool] = None,
        to: Optional[tuple] = None,
        read: Optional[bool] = None,
        version: Optional[str] = None,
    ):
        """Email Filter Generates a query string used to query the email backend. Email filter is used by the email client to store which emails have been run with which filters.
        The Filter uses `name` and `version` to uniquely identify itself.
        Queries based on: https://seosly.com/gmail-search-operators/

        Args:
            name: User defined name of filter. The name along with version is used to identify the filter internally to check which messages have been already run with a particular filter.
            run_completed: If True it will include messages that have already been processed.
            around:
            attachment:
            bcc:
            category:
            cc:
            filename:
            folder:
            important:
            label:
            keyword:
            newer_than:
            not_sender:
            older_than:
            phrase:
            sender:
            size: Minimum size of email in bytes
            size_larger:
            size_smaller:
            sent_after:
            sent_before:
            starred:
            to:
            read:
            version:
        """
        self.name = name
        self._newer_than = newer_than
        self._not_sender = not_sender
        self._older_than = older_than
        self._phrase = phrase
        self._size = size
        self._size_larger = size_larger
        self._size_smaller = size_smaller
        self._sent_after = sent_after
        self._sent_before = sent_before
        self._starred = starred
        self._keyword = keyword
        self._important = important
        self._filename = filename
        self._category = category
        self._bcc = bcc
        self._around = around
        self._attachment = attachment
        self._label = label
        self._folder = folder
        self._cc = cc
        self._to = to
        self._read = read
        self._sender = sender
        self._version = version

        self.save_folder = "processed_emails"

        self._validate()
        if run_completed:
            self.processed = set()
        else:
            self.processed = self.load_processed_ids()

    def _validate(self):
        """Validates inputs"""
        pass

    def filter_results(self, messages):
        """Removes messages in self.processed"""
        raise NotImplemented

    @property
    def processed_filename(self):
        return f"{self.save_folder}/{hash(self)}.bin"

    # def __del__(self):
    #     """Save Processed email ids"""
    #     print("exiting")
    #     data = set.union(self.load_processed_ids(), self.processed)
    #     if not os.path.exists(self.folder):
    #         os.makedirs(self.folder)
    #     with open(self.filename, 'wb') as file:
    #         pickle.dump(data, file)
    #     super(EmailFilter, self).__del__()

    def __hash__(self):
        hash_files = (
            self.name,
            self._version,
        )
        return int(hashlib.md5(str(hash_files).encode()).hexdigest(), 16)

    def load_processed_ids(self):
        """Loads A Set of ids that have been processed with this filter"""
        try:
            with open(self.processed_filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return set()

    def add_processed(self, email_id):
        print(email_id)
        self.processed.add(email_id)
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
        with open(self.processed_filename, "wb") as file:
            pickle.dump(self.processed, file)

    def get_filter_string(self):
        raise NotImplemented
