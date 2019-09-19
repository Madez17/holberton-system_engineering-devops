#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests
from sys import argv
import json

def number_of_subscribers(subreddit):
    API = requests.get('https://www.reddit.com/r/{}/about.json'.format(argv[1]))
    if API.status_code != 200:
        return 0
    else:
        req = json.loads(API.text)
        return (req.get('data').get('subscribers'))
