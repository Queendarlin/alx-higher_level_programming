#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n === 0) {
    return 1; // Base case: factorial of 0 is 1
  } else {
    return n * factorial(n - 1); // Recursive case: n * factorial(n-1)
  }
}

// Get the argument passed to the script
const arg = parseInt(process.argv[2]);

// Compute the factorial and print the result
console.log(factorial(arg));
