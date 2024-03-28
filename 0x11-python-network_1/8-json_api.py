#!/usr/bin/python3
"""
Sends a POST request to search for a user with a given letter and
displays the response.
"""

import requests
import sys

if __name__ == "__main__":
    my_url = "http://0.0.0.0:5000/search_user"
    the_letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the data to e sent in the POST request
    data = {'q': the_letter}

    # Send a POST request wit the data to the specified URL
    response = requests.post(my_url, data=data)

    try:
        # Check if the response is properly formatted and not empty
        json_response = response.json()
        if json_response:
            user_id = json_response.get('id')
            user_name = json_response.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
