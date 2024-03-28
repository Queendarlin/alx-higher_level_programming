#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the HTTP status code >= 400, prints an error message with the status code
"""

import requests
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]

    # Send a GET request to the specified UR
    response = requests.get(my_url)

    # Check if the status code is >= 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
