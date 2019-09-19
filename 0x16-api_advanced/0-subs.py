#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import requests
from sys import argv
import json


def number_of_subscribers(subreddit):
    user_agent = 'madez17'
    API = requests.get('https://www.reddit.com/r/{}/\
                       about.json'.format(argv[1]),
                       headers={'User-Agent': user_agent})
    if API.status_code == 200:
        req = json.loads(API.text)
        return (req.get('data').get('subscribers'))
    else:
        return 0
