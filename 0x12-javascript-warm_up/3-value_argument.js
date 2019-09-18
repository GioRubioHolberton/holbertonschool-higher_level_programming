#!/usr/bin/node
const myargv = process.argv;
if (myargv[2]) {
  console.log(myargv[2]);
} else {
  console.log('No argument');
}
