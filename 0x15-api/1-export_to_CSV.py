#!/usr/bin/python3
"""This script grabs the data from the API and exports to CSV"""

import csv
import requests
from sys import argv as av


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users/"

    user_data = requests.get(base_url + "{}".format(av[1])).json()
    todo_data = requests.get(base_url + "{}/todos".format(av[1])).json()

    # thank you Real Python for saving my bacon
    # https://realpython.com/python-csv/#writing-csv-files-with-csv
    with open("{}.csv".format(av[1]), mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="\"",
                            quoting=csv.QUOTE_ALL)

        for todo in todo_data:
            row = [
                    user_data.get("id"),
                    user_data.get("username"),
                    todo.get("completed"),
                    todo.get("title")
                    ]
            writer.writerow(row)
