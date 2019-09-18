#!/usr/bin/node
const my_num = parseInt(process.argv[2], 10);
if (isNaN(my_num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + my_num);
}
