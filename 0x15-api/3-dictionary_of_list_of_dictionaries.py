#!/usr/bin/python3
"""
Exports information of all employees to JSON format.
"""
import json
import requests

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com/"
    users = requests.get(uri + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        for u in users:
            for t in requests.get(uri + "todos",
                                  params={"userId": u.get("id")}).json():
                json.dump({
                    u.get("id"): [{
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": u.get("username")
                        }]}, jsonfile)
