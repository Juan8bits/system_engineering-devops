#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import csv
import json
import requests
from sys import argv

if __name__ == "__main__":

    url_users = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_users + argv[1])
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    usr_name = json.loads(users.text)['username']
    todo = json.loads(todo.text)
    tasks = list(i for i in todo if i['userId'] == int(argv[1]))
    succed_tasks = list(i for i in tasks if i['completed'] is True)

    with open(argv[1] + '.csv', 'w') as _file:
        objcsv = csv.writer(_file, quoting=csv.QUOTE_ALL)
        for i in tasks:
            objcsv.writerow([argv[1], usr_name, i['completed'], i['title']])
