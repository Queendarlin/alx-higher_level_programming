#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using urllib.
Displays the body of the response in a specific format.
"""

from urllib import request

if __name__ == "__main__":
    my_url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(my_url) as response:
        response_body = response.read()

        print("Body response:")
        print("\t- type:", type(response_body))
        print("\t- content:", response_body)
        print("\t- utf8 content:", response_body.decode('utf-8'))
