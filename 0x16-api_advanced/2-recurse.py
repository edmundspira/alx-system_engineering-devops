#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, count=None, hot_list=[]):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    param = {}
    if count is not None:
        param = {'count': count}
    url = 'https://reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'User-Agent': "Brandyn"}
    r = requests.get(url, headers=headers, params=param)
    try:
        after = r.json()['data'].get('count')
        for data in r.json()['data'].get('children'):
            hot_list.append(data['data'].get('title'))
        if after is not None:
            return(recurse(subreddit, after, hot_list))
        else:
            return(hot_list)
    except:
        return(None)
