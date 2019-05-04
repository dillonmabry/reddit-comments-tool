# Reddit Comments Analyzer
[![Build Status](https://travis-ci.org/dillonmabry/youtube-sentiment-helper.svg?branch=master)](https://travis-ci.org/dillonmabry/reddit-comments-tool)
[![Python 3.4](https://img.shields.io/badge/python-3.4-blue.svg)](https://www.python.org/downloads/release/python-340/)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

General package for reddit comments analysis, data manipulation, and other areas

## Install Instructions
```
pip install .
```

## How to Use
Required:
- Reddit Client ID
- Reddit Client Secret
- Reddit User Agent
- Subreddit
- List of Thread IDs for bulk extract of multiple Reddit threads
- Dictionary (Should match your regex search pattern, otherwise your headers will not match the data retrieved, for example: a defined copy/paste form for a reddit thread that users reply to, aka "Megathreads")
- Regex Pattern (for csv)

Extracting all comments for list of threads to csv with defined headers and search pattern:
```
import reddit_extract
reddit_extract.extract_comments_csv_bulk(<Reddit ClientID>, <Reddit ClientSecret>, <Reddit User Agent>, <Subreddit>, <Thread IDs>, <Dictionary Headers>)
```

Extracting all comments for list of threads to txt:
```
import reddit_extract
reddit_extract.extract_comments_txt_bulk(<Reddit ClientID>, <Reddit ClientSecret>, <Reddit User Agent>, <Subreddit>, <Thread IDs>)
```

Example:
```
import reddit_extract
threads = ['aw79c5', 'b7x7n1', 'am5uk7', 'bji681', 'abv2gl', '9klf8e']
search_pattern = r'Form: (.*)\n*Entity: (.*)\n*Pending: (.*)\n*Approved: (.*)\n*Standardized wait: (.*)\n*STATE: (.*)'
headers = {'Form': 'Form', 'Entity': 'Entity', 'Pending': 'Pending', 'Approved': 'Approved', 'Standardized Wait': 'Standardized Wait', 'STATE': 'STATE'}
reddit_extract.extract_comments_csv_bulk(<client_id>, <client_secret>, <user_agent>, 'nfa', threads, headers, search_pattern)
```

## Tests
```
python setup.py test
```
