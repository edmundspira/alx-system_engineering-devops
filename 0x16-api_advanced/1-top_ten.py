#!/usr/bin/python3
"""This module contains a function which queries the Reddit API"""
import requests
from sys import stderr


def top_ten(subreddit):
    """Prints the title of the first 10 hot posts listed by a given subreddit
    """

    if not isinstance(subreddit, str):
        stderr.write("Argument must be a string\n")
        return None

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return None

    data = response.json()
    for post in data.get('data', {}).get('children', []):
        print(post.get('data', {}).get('title', ''))
