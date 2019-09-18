#!/usr/bin/node
const numA = parseInt(process.argv[2]);
const numB = parseInt(process.argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(numA, numB));
