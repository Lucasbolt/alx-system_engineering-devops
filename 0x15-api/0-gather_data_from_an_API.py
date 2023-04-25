#!/usr/bin/python3
"""returns To-Do list information for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(uri + "todos", params={"userId": sys.argv[1]}).json()

    finished = []
    for t in todos:
        if t.get("completed") is True:
            finished.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    [print("\t {}".format(c)) for c in finished]
