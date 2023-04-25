#!/usr/bin/python3
"""
Exports information for a given employee ID to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(uri + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        for t in todos:
            json.dump({user_id: [{"task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": username
                    }]}, jsonfile)
