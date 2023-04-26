#!/usr/bin/python3
"""This module makes a request to a REST API and uses the data received"""
import json
import requests
from sys import stderr


base_url = "https://jsonplaceholder.typicode.com"


def gather_all_and_log_to_json():
    """Gathers data from an API, exports info about all tasks for all users"""

    # Send GET request to retrieve data on all users
    response = requests.get("{}/users".format(base_url))
    if response.status_code != 200:
        stderr.write("No users available\n")
        exit(1)

    file_name = "todo_all_employees.json"
    users = response.json()
    users_dict = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        name = user.get("name")

        # Send GET request to retrieve employee's tasks
        response = requests.get("{}/todos?userId={}".format(base_url, user_id))
        if response.status_code != 200:
            stderr.write(
                "TODO list not found for {}\n".format(name))
            exit(1)

        tasks = response.json()
        all_task_data = [{"username": username, "task": task.get(
            "title"), "completed": task.get("completed")} for task in tasks]

        users_dict[user_id] = all_task_data

    with open(file_name, mode="w", newline="") as json_file:
        json.dump(users_dict, json_file, indent=2)


if __name__ == "__main__":
    """Start of program"""
    gather_all_and_log_to_json()
