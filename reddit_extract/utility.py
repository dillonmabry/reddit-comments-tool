import pkg_resources
import csv
import os
from collections import Counter
import pandas as pd
from glob import glob
"""
Module for helper functions
"""


def load_string_from_file(filepath):
    """
    Load string from txt file
    Args:
        filepath: the path specified
    """
    try:
        with open(filepath, 'r') as myfile:
            data = myfile.read()
            return data
    except FileNotFoundError:
        raise


def find_duplicates(items):
    """
    Find duplicates in list and return
    Args:
        items: list of items
    """
    if len(items) != len(set(items)):
        duplicates = [item for item, count in Counter(
            items).items() if count > 1]
        return duplicates


def load_pattern_from_file():
    """
    Load regex pattern from file txt
    Args:
        filepath: the path specified
    """
    path = pkg_resources.resource_filename(__name__, 'resources/')
    template = load_string_from_file(path + 'search_template.txt')
    pattern = r''+template
    return pattern


def dump_csv(data, file, headers):
    """
    CSV Dictionary writer: dumps csv file from data of list of dicts
    Args:
        data: data to dump, format: list of dicts
        file: the file name to dump to
        headers: the csv headers
    """
    try:
        # Create directory for subreddit/thread
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception:
        raise


def merge_dump_csv(location, file):
    """
    Merge and dump all csvs in directory to a single csv
    Args:
        location: the location/directory of the csvs to merge
        file: the file name to dump to, final merged csv
    """
    try:
        dfs = [pd.read_csv(f, encoding='latin-1') for f in glob('{0}/*.csv'.format(location))]
        data = pd.concat(dfs, ignore_index=True)
        # Create directory for subreddit/thread
        os.makedirs(os.path.dirname(file), exist_ok=True)
        data.to_csv(file, index=False)
    except Exception:
        raise


def dump_txt(data, file, delimiter='\n'):
    """
    Txt file dump: dumps txt file from data of list of dicts
    Args:
        data: data to dump, format: list of dicts
        file: the file name to dump to
        delimeter: the delimeter to use for separating each comment text
    """
    try:
        # Create directory for subreddit/thread
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'w', newline='') as f:
            f.write(delimiter.join(data))
    except Exception:
        raise
