#!/usr/bin/python3
""" this scripts gets the first 10 hot posts on a subreddit """

import requests


def top_ten(subreddit):
    """ method that retrieves the first 10 hot posts """
    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".
                     format(subreddit),
                     headers={"User-Agent": "Custom"})

    if r.status_code == requests.codes.ok:
        for post in r.json()['data']['children']:
            post_data = post["data"]
            print(post_data["title"])
    else:
        print(None)
