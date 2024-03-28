#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using urllib.
Displays the body of the response in a specific format.
"""

from urllib import request

if __name__ == "__main__":
    my_url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(my_url) as response:
        my_data = response.read()

        print("Body response:")
        print("\t- type:", type(my_data))
        print("\t- content:", my_data)
        print("\t- utf8 content:", my_data.decode('utf-8'))
