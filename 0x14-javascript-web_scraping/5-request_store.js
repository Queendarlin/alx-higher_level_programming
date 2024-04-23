#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Write the body response to the specified file path
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      // If an error occurs while writing to the file, log the error
      console.error(err);
      process.exit(1);
    }
  });
});
