#!/bin/bash
# This script sends a POST request to the URL passed as an argument with email and subject parameters, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
