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
- Dictionary (If using CSV regex search: dictionary should match your "search_template.txt" under /resources for regex template customization)

Current usage:
```
import reddit_extract
reddit_extract.extract_comments_csv_bulk(<Reddit ClientID>, <Reddit ClientSecret>, <Reddit User Agent>, <Subreddit>, <Thread IDs>, <Dictionary Headers>)
```
or
```
import reddit_extract
reddit_extract.extract_comments_txt_bulk(<Reddit ClientID>, <Reddit ClientSecret>, <Reddit User Agent>, <Subreddit>, <Thread IDs>)
```
## Tests
```
python setup.py test
```
