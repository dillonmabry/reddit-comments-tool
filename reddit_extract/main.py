"""
Main module for data mining/gathering, persistence
"""
import argparse
from reddit_extract import RedditService
from reddit_extract import load_pattern_from_file
from reddit_extract import MultiProcess
from itertools import product


def main():
    """
    Main argparse for command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('client_id', help='Enter the reddit client id for API')
    parser.add_argument(
        'client_secret', help='Enter the reddit client secret for API')
    parser.add_argument(
        'user_agent', help='Enter the user agent for reddit API')
    parser.add_argument('subreddit', help='Enter the subredit to use')
    parser.add_argument('thread_id', help='Enter the thread id to use')
    args = parser.parse_args()
    reddit = RedditService(args.client_id, args.client_secret, args.user_agent)

    sample_threads = ['93t0b1', '9c74f5', '9klf8e',
                      '9t6fib', 'a2ot1d', 'abv2gl', 'am5uk7', 'aw79c5']
    sample_dict = {'Form': None, 'Entity': None, 'Pending': None,
                   'Approved': None, 'Wait': None, 'State': None}

    n_threads = len(sample_threads)
    multi = MultiProcess(threads=n_threads)
    p_args = list(zip(
        [args.subreddit] * n_threads,
        sample_threads,
        [load_pattern_from_file()] * n_threads,
        [sample_dict] * n_threads)
    )
    multi.process(operation=reddit.dump_pattern_comments_csv, items=p_args)


if __name__ == '__main__':
    main()
