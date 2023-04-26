#!/usr/bin/python3
"""This module makes a requests to a REST API and uses the data received"""
import csv
import requests
from sys import argv, stderr


base_url = "https://jsonplaceholder.typicode.com"


def gather_data_and_log(emp_id: str):
    """Gathers data from an API and saves data to CSV file"""
    # Send GET requests to retrieve employee data
    response = requests.get("{}/users/{}".format(base_url, emp_id))
    if response.status_code != 200:
        stderr.write("Employee with id [{}] not found\n".format(emp_id))
        exit(1)

    username = response.json().get("username")

    # Send GET requests to retrieve employee's todos
    response = requests.get("{}/todos?userId={}".format(base_url, emp_id))
    if response.status_code != 200:
        stderr.write("TODO list not found\n")
        exit(1)

    todos = response.json()
    file_name = "{}.csv".format(emp_id)

    # Log employee data
    with open(file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            status = "True" if todo.get("completed") else "False"
            writer.writerow([
                emp_id,
                username,
                status,
                todo.get("title"),
            ])

    print("Successfully exported data for {} to {}".format(emp_id, file_name))


if __name__ == "__main__":
    """Start of program"""
    if len(argv) != 2 or not argv[1].isdigit():
        stderr.write("Usage: {} <id>\n".format(argv[0]))
        exit(1)

    gather_data_and_log(argv[1])
