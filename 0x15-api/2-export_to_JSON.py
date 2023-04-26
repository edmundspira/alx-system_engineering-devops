#!/usr/bin/python3
"""This module makes a requests to a REST API and uses the data received"""
import json
import requests
from sys import argv, stderr


base_url = "https://jsonplaceholder.typicode.com"


def gather_data_and_log_to_json(user_id: str):
    """Gathers data from an API and export info about all tasks for employee"""

    # Send GET requests to retrieve employee data
    response = requests.get("{}/users/{}".format(base_url, user_id))
    if response.status_code != 200:
        stderr.write("Employee with id [{}] not found\n".format(user_id))
        exit(1)

    employee = response.json()

    # Send GET requests to retrieve employee's tasks
    response = requests.get("{}/todos?userId={}".format(base_url, user_id))
    if response.status_code != 200:
        stderr.write("TODO list not found\n")
        exit(1)

    tasks = response.json()

    file_name = "{}.json".format(user_id)
    all_task_data = [{"task": task.get("title"), "completed": task.get(
        "completed"), "username": employee.get("username")} for task in tasks]

    with open(file_name, mode="w", newline="") as json_file:
        json.dump({user_id: all_task_data}, json_file, indent=2)


if __name__ == "__main__":
    """Start of program"""
    if len(argv) != 2 or not argv[1].isdigit():
        stderr.write("Usage: {} <id>\n".format(argv[0]))
        exit(1)

    gather_data_and_log_to_json(argv[1])
