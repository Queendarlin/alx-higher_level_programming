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

  // Define a function to fetch and print character names in order
  const printCharacters = (charactersUrls, index) => {
    if (index >= charactersUrls.length) {
      return;
    }

    // Make a GET request to fetch character details
    request.get(charactersUrls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        process.exit(1);
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Call the function recursively for the next character
      printCharacters(charactersUrls, index + 1);
    });
  };

  // Start printing characters in order
  printCharacters(movieData.characters, 0);
});
