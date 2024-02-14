#!/usr/bin/node

const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
// make a Get request
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Create an array to store all promises
    const promises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    // Wait for all promises to resolve
    Promise.all(promises)
      .then(characterNames => {
        // Once all promises are resolved, log the character names
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});
