#!/usr/bin/node
const mynum = parseInt(process.argv[2], 10);
if (isNaN(mynum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + mynum);
}
