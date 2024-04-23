#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the API URL from command-line argument
const apiUrl = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = 18;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Parse the JSON response body
  const moviesData = JSON.parse(body);

  // Filter the movies where "Wedge Antilles" is present
  const moviesWithWedge = moviesData.results.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  // Print the number of movies where "Wedge Antilles" is present
  console.log(moviesWithWedge.length);
});
