#!/usr/bin/python3
"""This module queries the `Reddit` API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Uses recursion to return the list of hot articles for given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 25, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after', None)

    for post in posts:
        title = post.get('data', {}).get('title', '')
        hot_list.append(title)

    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
