#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using the requests
package. Displays the body of the response in a specific format.
"""

import requests

if __name__ == "__main__":
    my_url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(my_url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
