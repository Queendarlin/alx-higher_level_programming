#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the API URL from command-line argument
const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Create an object to store the count of completed tasks by user ID
  const completedTasksByUser = {};

  // Loop through the todos and count completed tasks by user ID
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print the object containing the count of completed tasks by user ID
  console.log(completedTasksByUser);
});
