from unittest import TestCase
from reddit_extract import RedditService


class TestReddit(TestCase):
    """ Test reddit API """
    @classmethod
    def setUpClass(self):
        """ Setup """
        self.mock = RedditService('abc', 'def', 'ghi')

    def test_service_attributes(self):
        """ Ensure service attributes """
        mock_service = self.mock
        self.assertTrue(hasattr(mock_service, 'get_all_comments'))
        self.assertTrue(hasattr(mock_service, 'get_pattern_comments'))
        self.assertTrue(hasattr(mock_service, 'dump_all_comments_txt'))
        self.assertTrue(hasattr(mock_service, 'dump_pattern_comments_csv'))
        self.assertTrue(hasattr(mock_service, '__init__'))

    def test_dump_txt_comments(self):
        #TODO: Test dumping txt comments, refactor separation of concern for Reddit class
        self.assertTrue(True)

    def test_dump_csv_comments(self):
        #TODO: Test dumping csv comments, refactor separation of concern for Reddit class
        self.assertTrue(True)

    @classmethod
    def tearDownClass(self):
            """ Tear down """
            del self.mock
