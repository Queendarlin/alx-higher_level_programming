#!/usr/bin/node

// Check if the first argument is missing or not a number
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]); // Convert the argument to a number
  let i = 0;
  
  // Loop to print "C is fun" x times
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
