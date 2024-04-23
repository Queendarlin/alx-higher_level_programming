#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Get the file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both file path and content are provided as arguments
if (!filePath || !content) {
  console.error('Provide the file path and content as arguments');
  process.exit(1);
}

// Write the content to the file asynchronouslyfs.writeFile(filePath, content, 'utf-8', (err) => {
fs.writeFile(filePath, content, (err) => {
    // If an error occurs during writing, log the error and exit with error code 1
    console.error(err);
    process.exit(1);
  }
});
