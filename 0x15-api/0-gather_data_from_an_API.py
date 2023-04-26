#!/usr/bin/python3
"""This module makes a requests to a REST API and uses the data received"""
import requests
from sys import argv, stderr


base_url = "https://jsonplaceholder.typicode.com"


def gather_data_from_an_api(emp_id: str):
    """Gathers data from an API"""
    # Send GET requests to retrieve employee data
    response = requests.get("{}/users/{}".format(base_url, emp_id))
    if response.status_code != 200:
        stderr.write("Employee with id [{}] not found\n".format(emp_id))
        exit(1)

    employee_name = response.json().get("name")

    # Send GET requests to retrieve employee's todos
    response = requests.get("{}/todos?userId={}".format(base_url, emp_id))
    if response.status_code != 200:
        stderr.write("TODO list not found\n")
        exit(1)

    todos = response.json()

    # Calculate the total number of completed tasks
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    no_of_completed_tasks = len(completed_tasks)

    # Print employee data and todos
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          no_of_completed_tasks, len(todos)))
    for todo in completed_tasks:
        print("\t {}".format(todo.get("title")))


if __name__ == "__main__":
    """Start of program"""
    if len(argv) != 2 or not argv[1].isdigit():
        stderr.write("Usage: {} <id>\n".format(argv[0]))
        exit(1)

    gather_data_from_an_api(argv[1])
