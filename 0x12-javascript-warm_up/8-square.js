#!/usr/bin/node
const myC = parseInt(process.argv[2]);
if (isNaN(myC)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < myC; i++) {
      let myX = '';
    for (let j = 0; j < myC; j++) {
      myX = 'X';
    }
    console.log('C is fun');
  }
}
