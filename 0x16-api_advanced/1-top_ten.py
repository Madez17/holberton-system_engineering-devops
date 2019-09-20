#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    user_agent = 'Madez'
    API = requests.get('https://www.reddit.com/r/' +
                       subreddit + '/hot.json?limit=10',
                       headers={'User-Agent': user_agent},
                       allow_redirects=False)

    if API.status_code == 200:
        req = API.json()
        for children in req.get('data').get('children'):
            print(children.get('data').get('title'))
    else:
        print(None)
