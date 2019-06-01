from unittest import TestCase

from reddit_extract import find_duplicates
from reddit_extract import load_string_from_file
from reddit_extract import load_pattern_from_file


class TestUtility(TestCase):
    """ Test Utilities """

    def test_find_duplicates(self):
        l = ["test", "test1", "test2", "test"]
        dups = find_duplicates(l)
        self.assertEquals(len(dups), 1)

    def test_load_string_from_file(self):
        with self.assertRaises(FileNotFoundError):
            load_string_from_file('test_file_not_found.txt')
