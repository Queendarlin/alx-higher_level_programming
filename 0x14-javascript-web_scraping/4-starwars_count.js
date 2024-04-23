#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the API URL from command-line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Parse the JSON response body
  const moviesData = JSON.parse(body);

  // Count the number of movies where "Wedge Antilles" is present
  const moviesWithWedgeCount = moviesData.results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0);

  // Print the number of movies where "Wedge Antilles" is present
  console.log(moviesWithWedgeCount);
});
