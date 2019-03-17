"""
Main module for data mining/gathering, persistence
"""
import argparse
from reddit_extract import load_pattern_from_file
from reddit_extract import RedditService
from reddit_extract import MultiProcess


def extract_comments_csv_bulk(client_id,
                              client_secret,
                              user_agent,
                              subreddit,
                              thread_ids,
                              dictionary
                              ):
    reddit = RedditService(client_id, client_secret, user_agent)
    n_threads = len(thread_ids)
    multi = MultiProcess(threads=n_threads)
    p_args = list(zip(
        [subreddit] * n_threads,
        thread_ids,
        [load_pattern_from_file()] * n_threads,
        [dictionary] * n_threads)
    )
    multi.process(
        operation=reddit.dump_pattern_comments_csv, items=p_args)


def extract_comments_txt_bulk(client_id, client_secret, user_agent, subreddit, thread_ids):
    reddit = RedditService(client_id, client_secret, user_agent)
    n_threads = len(thread_ids)
    multi = MultiProcess(threads=n_threads)
    p_args = list(zip(
        [subreddit] * n_threads,
        thread_ids)
    )
    multi.process(
        operation=reddit.dump_all_comments_txt, items=p_args)


def main():
    """
    Main argparse for command line
    Parse a single reddit thread with all comments as txt
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
    reddit.dump_all_comments_txt(
        subreddit=args.subreddit, thread_id=args.thread_id)


if __name__ == '__main__':
    main()
