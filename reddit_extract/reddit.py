import praw
import re
from reddit_extract import dump_csv, dump_txt


class RedditService(object):

    def __init__(self, client_id, client_secret, user_agent):
        """
        Create reddit service
        Args:
            client_id: reddit client ID
            client_secret: reddit client secret
            user_agent: unique user agent for API
        """
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)

    def get_all_comments(self, subreddit, thread_id):
        """
        Get all comments for a specific subreddit thread
        Args:
            subreddit: the subreddit specified
            thread_id: the unique ID of the thread
        """
        submission = self.reddit.submission(id=thread_id)
        submission.comment_sort = 'new'
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]  # Seed with top-level
        extracted_values = []
        while comment_queue:  # Load more comments
            comment = comment_queue.pop(0)
            extracted_values.append(comment.body)
            comment_queue.extend(comment.replies)
        return extracted_values

    def get_pattern_comments(self, subreddit, thread_id, pattern, dictionary):
        """
        Get all comments for a specific subreddit thread based on pattern
        Args:
            subreddit: the subreddit specified
            thread_id: the unique ID of the thread
            pattern: the regex pattern to search
            dictionary: the dictionary based on the regex search group matched
        Returns list of dicts based on the supplied dictionary object
        """
        submission = self.reddit.submission(id=thread_id)
        submission.comment_sort = 'new'
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]  # Seed with top-level
        extracted_values = []
        while comment_queue:  # Load more comments
            comment = comment_queue.pop(0)
            m = re.match(pattern, comment.body, re.IGNORECASE | re.MULTILINE)
            if m is not None:
                for index, key in enumerate(dictionary):
                    dictionary[key] = m.group(index + 1)
                extracted_values.append(dictionary.copy())
            comment_queue.extend(comment.replies)
        return extracted_values

    def dump_all_comments_txt(self, subreddit, thread_id):
        """
        Dump all comments for a specific subreddit thread via txt
        Args:
            subreddit: the subreddit specified
            thread_id: the unique ID of the thread
        """
        comments = self.get_all_comments(subreddit, thread_id)
        print('{0} total comments retrieved for subreddit {1} and thread {2}'
              .format(str(len(comments)), subreddit, thread_id))
        try:
            dump_txt(
                data=comments,
                file='./{0}/{1}_comments.txt'.format(subreddit, thread_id,
                                                     delimiter='\n')
            )
            return True
        except Exception:
            raise

    def dump_pattern_comments_csv(self, subreddit, thread_id, pattern, dictionary):
        """
        Dump all comments for a specific subreddit thread based on pattern
        Args:
            subreddit: the subreddit specified
            thread_id: the unique ID of the thread
            pattern: the regex pattern to search
            dictionary: dictionary to extract based on the supplied search_template.txt
        Dumps comments to file specified
        """
        comments = self.get_pattern_comments(
            subreddit, thread_id, pattern, dictionary)
        print('{0} total comments retrieved for subreddit {1} and thread {2}'
              .format(str(len(comments)), subreddit, thread_id))
        try:
            dump_csv(
                data=comments,
                file='./{0}/{1}_comments.csv'.format(subreddit, thread_id),
                headers=list(dictionary.keys())  # headers as keys from dict
            )
            return True
        except Exception:
            raise
