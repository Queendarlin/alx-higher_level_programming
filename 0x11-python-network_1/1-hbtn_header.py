#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

from urllib import request
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]

    with request.urlopen(my_url) as response:
        print(response.headers['X-Request-Id'])
