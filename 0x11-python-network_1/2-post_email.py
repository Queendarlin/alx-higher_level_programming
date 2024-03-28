#!/usr/bin/python3
"""
Sends a POST request with an email parameter to a specified URL
and displays the body of the response (decoded in utf-8).
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request and read the response
    with request.urlopen(url, data=data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
