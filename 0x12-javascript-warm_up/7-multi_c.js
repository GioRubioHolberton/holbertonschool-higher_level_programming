#!/usr/bin/node
const myC = parseInt(process.argv[2]);
if (isNaN(myC)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myC; i++) {
    console.log('C is fun');
  }
}

