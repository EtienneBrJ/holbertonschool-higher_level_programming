#!/usr/bin/node
const request = require('request');
// const fs = require('fs');
const apiUrl = process.argv[2]
request.get(apiUrl, function (error, response, body) {
      const content = JSON.parse(body)
      if ()
    });


