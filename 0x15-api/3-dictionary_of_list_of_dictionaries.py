#!/usr/bin/python3
"""Simple example of exporting user data to json"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users/"
    num_of_employees = len(requests.get(base_url).json())

    all_users_data = {}
    for i in range(num_of_employees):
        # Incrementing i by 1 since user IDs start from 1
        user_data = requests.get(base_url + "{}".format(i + 1)).json()
        todo_data = requests.get(base_url + "{}/todos".format(i + 1)).json()

        current_user_tasks = []
        for todo in todo_data:
            task = {
                "username": user_data.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            current_user_tasks.append(task)

        # Store data for each user
        all_users_data[i + 1] = current_user_tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_users_data, file)
