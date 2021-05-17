#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        Return that prints the title of the first 10 hot posts.
    """
    req = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit), allow_redirects=False)
    if req.status_code == '200':
        list_titles = req.json().get('data').get('children')
        for title in list_titles:
            print(title.get('data').get('title'))
    else:
        print('None')
