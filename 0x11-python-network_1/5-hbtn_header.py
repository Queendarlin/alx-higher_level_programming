#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]

    response = requests.get(my_url)
    print(response.headers['X-Request-Id'])
