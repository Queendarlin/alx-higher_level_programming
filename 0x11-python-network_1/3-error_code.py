#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response
(decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code
in case of an error.
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
