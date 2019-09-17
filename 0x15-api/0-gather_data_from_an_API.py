#!/usr/bin/python3
""" consumir api filter by user and show task did"""
import requests
from sys import argv

if __name__ == '__main__':
    API_all = requests.get('https://jsonplaceholder.typicode\
                           .com/todos?userId={}'.format(argv[1]))
    API_USR = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                           .format(argv[1]))

    req_a_all = API_all.json()
    req_a_usr = API_USR.json()

    list_about_employee = []
    for task in req_a_all:
        if task.get('completed') is False:
            pass
        else:
            list_about_employee.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(req_a_usr.get('name'),
                  len(list_about_employee), len(req_a_all)))
    for more_task in list_about_employee:
        print('\t{}'.format(more_task))
