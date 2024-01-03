#!/usr/bin/python3
"""Simple example of accessing a REST API from the web. Need more studying"""

import requests
from sys import argv as av


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users/"

    user_data = requests.get(base_url + "{}".format(av[1])).json()
    todo_data = requests.get(base_url + "{}/todos".format(av[1])).json()

    employee_name = user_data.get("name")
    # print(employee_name)
    finished_tasks = []
    finished = 0

    for todo in todo_data:
        if todo.get("completed"):
            finished_tasks.append(todo)
            finished += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, finished, len(todo_data)))

    for task in finished_tasks:
        print("\t {}".format(task.get("title")))
