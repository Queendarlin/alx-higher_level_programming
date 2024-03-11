#!/usr/bin/node

// Define the myObject object
const myObject = {
  type: 'object',
  value: 12,
  // Define the incr function
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

// Call incr function to increment the value
myObject.incr();
console.log(myObject);

// Call incr function again
myObject.incr();
console.log(myObject);

// Call incr function again
myObject.incr();
console.log(myObject);
