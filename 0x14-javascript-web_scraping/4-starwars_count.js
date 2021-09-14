#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const bodyResponse = JSON.parse(body).results.filter((obj) => {
    return obj.characters.filter((url) => { return url.endsWith('/18/'); }).length;
  }).length;
  console.log(bodyResponse);
});
