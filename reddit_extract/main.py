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
                              headers,
                              search_pattern
                              ):
    """
    Extract all comments to csv file for a subreddit and list of threads for pattern
    Args:
        client_id: reddit api client id
        client_secret: reddit api secret
        user_agent: custom identifier of your dev agent (Ex. <reddit_user_id>)
        subreddit: subreddit
        thread_ids: list of threads for the subreddit
        headers: extracted csv headers, should match search_pattern
        search_pattern: regex defined search pattern, example: r'<search_pattern>'
    """
    reddit = RedditService(client_id, client_secret, user_agent)
    n_threads = len(thread_ids)
    multi = MultiProcess(threads=n_threads)
    # For search_pattern, can also use search_template.txt in resources to copy/paste long patterns
    p_args = list(zip(
        [subreddit] * n_threads,
        thread_ids,
        [search_pattern] * n_threads,
        [headers] * n_threads)
    )
    multi.process(
        operation=reddit.dump_pattern_comments_csv, items=p_args)


def extract_comments_txt_bulk(client_id, client_secret, user_agent, subreddit, thread_ids):
    """
    Extract all comments to text file for a subreddit and list of threads
    Args:
        client_id: reddit api client id
        client_secret: reddit api secret
        user_agent: custom identifier of your dev agent (Ex. <reddit_user_id>)
        subreddit: subreddit
        thread_ids: list of threads for the subreddit
    """
    reddit = RedditService(client_id, client_secret, user_agent)
    n_threads = len(thread_ids)
    multi = MultiProcess(threads=n_threads)
    p_args = list(zip(
        [subreddit] * n_threads,
        thread_ids)
    )
    multi.process(
        operation=reddit.dump_all_comments_txt, items=p_args)


def merge_subreddit_threads(subreddit, file):
    """
    Merge subreddit directory thread csvs into single csv
    Args:
        subreddit: the subreddit directory of the extracted csv files
        file: the file location to save as
    """
    RedditService.merge_csv_bulk(subreddit, file)


def main():
    """
    Main argparse for command line
    Parse a single reddit thread and dump all replies to txt
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
