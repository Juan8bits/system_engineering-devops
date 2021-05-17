#!/usr/bin/python3
"""
    Recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """
        Return that prints the title of the first 10 hot posts.
    """
    header = {'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    req = requests.get('https://www.reddit.com/r/{}/hot.json'
                       .format(subreddit), allow_redirects=False,
                       headers=header, params=params)
    if req.status_code == 200:
        results = req.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for post in results.get("children"):
            hot_list.append(post.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    else:
        return None
