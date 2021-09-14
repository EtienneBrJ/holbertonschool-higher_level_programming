#!/usr/bin/node
const request = require('request');
// const fs = require('fs');
const apiUrl = process.argv[2];
request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    const dic = {};
    let i = 0;

    for (i; i < content.length; i++) {
      if (!(content[i].userId in dic)) {
        if (content[i].completed === true) {
          dic[content[i].userId] = 0;
        }
      }
      if (content[i].completed === true) {
        dic[content[i].userId] += 1;
      }
    }
    console.log(dic);
  }
});
