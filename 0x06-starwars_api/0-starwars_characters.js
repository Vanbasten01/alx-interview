#!/usr/bin/node

const request = require('request');

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
// make a Get request
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
