#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints first 10 titles of hot posts"""
    hot_posts = requests.get(
        'https://api.reddit.com/r/{}/hot'.format(subreddit),
        headers={'User-Agent': 'Brandyn'}
    ).json()
    try:
        i = 0
        while (i < 10):
            post = hot_posts['data']['children'][i]
            print(post['data']['title'])
            i += 1
    except:
        print(None)
