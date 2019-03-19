import pkg_resources
import csv
import os
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
    except FileNotFoundError as e:
        raise e


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
    if data is None or len(data) == 0:
        print("No data supplied, aborting dump")
        return
    # Create directory for subreddit/thread
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def dump_txt(data, file, delimiter='\n'):
    """
    Txt file dump: dumps txt file from data of list of dicts
    Args:
        data: data to dump, format: list of dicts
        file: the file name to dump to
        delimeter: the delimeter to use for separating each comment text
    """
    if data is None or len(data) == 0:
        print("No data supplied, aborting dump")
        return
    # Create directory for subreddit/thread
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, 'w', newline='') as f:
        try:
            f.write(delimiter.join(data))
        except Exception:
            raise
