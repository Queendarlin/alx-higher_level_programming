#!/usr/bin/node

// Define the myObject object
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Define the incr function using dot notation
myObject.incr = function () {
  this.value++;
};

// Call incr function to increment the value
myObject.incr();
console.log(myObject);

// Call incr function again
myObject.incr();
console.log(myObject);

// Call incr function again
myObject.incr();
console.log(myObject);
