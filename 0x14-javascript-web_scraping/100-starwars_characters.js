#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the Movie ID from command-line argument
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

  // Print all characters of the movie
  movieData.characters.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
