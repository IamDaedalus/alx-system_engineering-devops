#!/usr/bin/python3
""" this script gets the subscriber count from a subreddit """

import requests


def number_of_subscribers(subreddit):
    """ method that retrieves the number of subscribers in a subreddit """
    r = requests.get("https://www.reddit.com/r/{}/about.json".
                     format(subreddit),
                     headers={"User-Agent": "Custom"})

    try:
        if r.status_code == requests.codes.ok:
            return r.json()['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
