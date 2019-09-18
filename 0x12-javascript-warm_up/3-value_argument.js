#!/usr/bin/node
const my_argv = process.argv;
if (my_argv[2]) {
  console.log(my_argv[2]);
} else {
  console.log('No argument');
}
