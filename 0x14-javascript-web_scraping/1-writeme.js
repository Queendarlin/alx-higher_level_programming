#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Get the file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the file asynchronously
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurs during writing, log the error and exit with error code 1
    console.error(err);
    process.exit(1);
  }
});
