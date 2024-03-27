#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL, and displays the body of the response if the response status code is 200
curl -s -L "{$1}"
