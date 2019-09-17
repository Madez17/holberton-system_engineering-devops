#!/usr/bin/python3
""" Script that export file in format csv"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    API_all = requests.get('https://jsonplaceholder.typicode.com/\
                           todos?userId={}'.format(argv[1]))
    API_USR = requests.get('https://jsonplaceholder.typicode.com/\
                            users/{}'.format(argv[1]))
    req_a_all = API_all.json()
    req_a_usr = API_USR.json()

    with open('{}.csv'.format(argv[1]), mode='w') as employee_file:
        em_writer = csv.writer(employee_file, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_ALL)
        for line in req_a_all:
            em_writer.writerow([line.get('userId'),
                               req_a_usr.get('username'),
                               line.get('completed'),
                               line.get('title')])
