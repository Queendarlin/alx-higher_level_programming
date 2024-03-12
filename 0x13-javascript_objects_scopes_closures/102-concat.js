#!/usr/bin/node

const fs = require('fs');

// Extract file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

// Read the content of the source files
const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');

// Concatenate the content of the source files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);

console.log(`Files ${sourceFile1} and ${sourceFile2} have been concatenated to ${destinationFile}`);
