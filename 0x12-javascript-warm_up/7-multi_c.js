#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const numOccurrences = parseInt(arg);

// Check if the conversion is successful and if it's a positive integer
if (!isNaN(numOccurrences) && numOccurrences > 0) {
  // Loop to print "C is fun" numOccurrences times
  let output = '';
  for (let i = 0; i < numOccurrences; i++) {
    output += 'C is fun\n';
  }
  console.log(output.trim()); // Print the output after removing the trailing newline
} else {
  console.log('Missing number of occurrences');
}
