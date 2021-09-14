#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const charactersURLs = JSON.parse(body).characters;

  for (const line of charactersURLs) {
    request(line, (err, response, body) => {
      if (err) {
        console.error(err);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
