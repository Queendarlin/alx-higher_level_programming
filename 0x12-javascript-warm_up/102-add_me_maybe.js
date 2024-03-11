#!/usr/bin/node

// Define the addMeMaybe function
function addMeMaybe (number, theFunction) {
  // Increment the number by 1
  number += 1;
  // Call theFunction with the incremented number as argument
  theFunction(number);
}

// Export the addMeMaybe function to make it visible from outside
module.exports.addMeMaybe = addMeMaybe;
