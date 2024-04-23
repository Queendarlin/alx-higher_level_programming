#!/usr/bin/node
// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the URL from command-line argument
const url = process.argv[2];

// Make a GET request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Log the status code of the response
  console.log(`code: ${response.statusCode}`);
});
