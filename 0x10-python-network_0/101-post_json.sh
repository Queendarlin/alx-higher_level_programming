#!/bin/bash
# This script sends a JSON POST request to the URL passed as the first argument, using the contents of a file passed as the second argument, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
