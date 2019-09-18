#!/usr/bin/node
const myC = parseInt(process.argv[2]);
function factorial (x) {
  if (x > 0) {
    return (x * factorial(x - 1));
  } else {
    return 1;
  }
}
console.log(factorial(myC));
