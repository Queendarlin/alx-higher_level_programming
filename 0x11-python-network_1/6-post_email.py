#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    my_url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in the POST request
    data = {'email': email}

    # Send a POST request with the data to the specified URL
    response = requests.post(my_url, data=data)

    # Print the body of the response
    print(response.text)
