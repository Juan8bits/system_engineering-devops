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
    header = {'User-Agent':'Chrome/90.0.4430.212 Safari/537.36'}
    req = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit), allow_redirects=False,
                       headers=header)
    if req.status_code == 200:
        list_titles = req.json().get('data').get('children')
        for title in list_titles:
            print(title.get('data').get('title'))
    else:
        print(None)
