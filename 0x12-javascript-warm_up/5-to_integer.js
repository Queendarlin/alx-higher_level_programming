#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt() and check if it's a valid integer
const number = parseInt(arg);

// Check if the conversion is successful and print the output accordingly
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
