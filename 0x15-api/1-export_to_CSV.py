#!/usr/bin/python3
"""
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv


def main():
    """ returns TODO list """
    total = 0
    complete = 0
    user_url = "https://jsonplaceholder.typicode.com/users/"
    task_url = "https://jsonplaceholder.typicode.com/todos?userId="
    user = requests.get('{}{}'.format(user_url, argv[1])).json()
    tasks = requests.get('{}{}'.format(task_url, argv[1])).json()

    for task in tasks:
        task['username'] = user['username']
        del task['id']

    with open("{}.csv".format(argv[1]), 'w') as f:
        fieldnames = ["userId", "username", "completed", "title"]
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames,
                                     quoting=csv.QUOTE_ALL)
        dict_writer.writerows(tasks)

if __name__ == "__main__":
    main()
