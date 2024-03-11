#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Check if an argument is provided and print it, else print "No argument"
if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
