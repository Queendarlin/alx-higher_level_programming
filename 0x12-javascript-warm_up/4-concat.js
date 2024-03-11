#!/usr/bin/node

// Get the first and second arguments passed to the script
const arg1 = process.argv[2] || 'undefined'; // If no argument provided, set to 'undefined'
const arg2 = process.argv[3] || 'undefined'; // If no second argument provided, set to 'undefined'

// Print the arguments in the specified format
console.log(`${arg1} is ${arg2}`);
