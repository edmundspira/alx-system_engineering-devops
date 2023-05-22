#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def count_words_helper(word: str, text: str) -> int:
    """
    Count the number of occurrences of a word in a string.
    """
    return text.lower().split().count(word.lower())


def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Recursively count the number of occurrences of keywords in the titles
    of hot articles in a subreddit.
    """

    if count_dict is None:
        count_dict = {}
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    for post in data.get("data", {}).get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in word_list:
            count_dict[word] = count_dict.get(
                word, 0) + count_words_helper(word, title)
        count_dict = count_words(subreddit, word_list,
                                 count_dict, data.get("data", {}).get("after"))

    if after is None and count_dict is not None:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print('{}: {}'.format(word.lower(), count))
