#!/usr/bin/node

const url = 'http://swapi.co/api/films/' + process.argv[2];
const req = require('request');
req(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
