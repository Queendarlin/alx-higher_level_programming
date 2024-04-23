#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the movie ID from command-line argument
const movieId = process.argv[2];

// Construct the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // If an error occurs during the request, log the error
    console.error(error);
    process.exit(1);
  }

  // Parse the JSON response body
  const movieData = JSON.parse(body);

  // Check if the movie data contains the title
  if (movieData.title) {
    // Print the title of the movie
    console.log(movieData.title);
  } else {
    console.error('Movie not found');
    process.exit(1);
  }
});
