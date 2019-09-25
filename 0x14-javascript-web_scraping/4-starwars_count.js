#!/usr/bin/node

const url = process.argv[2];
const req = require('request');
req(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    let num = 0;
    const rta = JSON.parse(body).rta;
    for (let i = 0; i < rta.length; i++) {
      if (rta[i].characters.includes('https://swapi.co/api/people/18/')) {
        num++;
      }
    }
    console.log(num);
  }
});
