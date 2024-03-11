#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Convert arguments to integers and sort them in descending order
const integers = args.map(Number).sort((a, b) => b - a);

// Check if no arguments are passed or only one argument is passed
if (integers.length === 0 || integers.length === 1) {
  console.log(0);
} else {
  // Print the second biggest integer
  console.log(integers[1]);
}
