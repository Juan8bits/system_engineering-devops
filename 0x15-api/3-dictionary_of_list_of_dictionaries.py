#!/usr/bin/python3
""" Script that extend your Python script to export data
    in the JSON format.
"""
import json
import requests

if __name__ == "__main__":

    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(url_users).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": u.get('username')
            } for i in requests.get(url_todo,
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
