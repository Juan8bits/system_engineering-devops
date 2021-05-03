#!/usr/bin/python3
""" Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    url_users = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_users + argv[1])
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    user_name = json.loads(users.text)['name']
    todo = json.loads(todo.text)
    tasks = list(i for i in todo if i['userId'] == int(argv[1]))
    succed_tasks = list(i for i in tasks if i['completed'] is True)

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(succed_tasks), len(tasks)))
    [print('     ' + task['title']) for task in succed_tasks]
