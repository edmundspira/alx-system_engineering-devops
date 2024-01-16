#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Use reddit api to get number of subscribers to a subreddit
    """
    url = 'https://reddit.com/r/' + subreddit + '/about/.json'
    headers = {'User-Agent': "Brandyn"}
    r = requests.get(url, headers=headers)
    try:
        return(r.json().get('data').get('subscribers'))
    except:
        return(0)
