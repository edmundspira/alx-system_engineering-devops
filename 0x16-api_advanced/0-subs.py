#!/usr/bin/python3
"""This module sends request to the reddit api"""
import requests


def number_of_subscribers(subreddit: str) -> int:
    """This returns the number of subscribers for a given subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']['subscribers']
