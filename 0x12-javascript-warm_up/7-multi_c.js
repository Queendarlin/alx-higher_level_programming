#!/usr/bin/node

// Get the first argument passed to the script
const arg = process.argv[2];

// Convert the argument to an integer using parseInt()
const numOccurrences = parseInt(arg);

// Check if the conversion is successful and if it's a positive integer
if (!isNaN(numOccurrences) && numOccurrences > 0) {
  // Loop to print "C is fun" numOccurrences times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
