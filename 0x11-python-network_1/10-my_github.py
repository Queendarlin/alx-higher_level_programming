#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to display your GitHub user ID.
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    authentication = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=authentication)

    user_data = response.json()
    user_id = user_data.get("id")
    print(user_id)
