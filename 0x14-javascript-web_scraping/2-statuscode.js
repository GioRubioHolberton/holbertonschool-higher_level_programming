#!/usr/bin/node

const url = process.argv[2];
const req = require('request');
req(url, function (err, resp) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + resp.statusCode);
  }
});
