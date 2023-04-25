#!/usr/bin/python3
"""
Exports Do-Do list information for a given employee ID to CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(uri + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                    [user_id, username, t.get("completed"), t.get("title")]
                    )
