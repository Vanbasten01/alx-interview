#!/usr/bin/node

const request = require('request');

function printchars (filmId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
  // make a Get request
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error: ', error);
    } else if (response.statusCode !== 200) {
      console.log('status_code: ', response.statusCode);
    } else {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;
      characters.forEach(characterUrl => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error: ', error);
          } else if (response.statusCode !== 200) {
            console.log('status_code: ', response.statusCode);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
  });
}

const filmId = process.argv[2];

if (filmId) {
  printchars(filmId);
}
