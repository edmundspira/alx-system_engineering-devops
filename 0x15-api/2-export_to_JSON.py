#!/usr/bin/python3
"""
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS,"username":"USERNAME"}},{"task":"TASK_TITLE","completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}
File name must be: USER_ID.json
"""
from json import dump
import requests
from sys import argv


if __name__ == "__main__":
    new_list = []
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    for task in requests.get(url).json():
        if user["id"] == task["userId"]:
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user["username"]
            new_list.append(task_dict)
    result = {str(argv[1]): new_list}
    with open(argv[1] + ".json", 'w') as file:
        dump(result, file)
