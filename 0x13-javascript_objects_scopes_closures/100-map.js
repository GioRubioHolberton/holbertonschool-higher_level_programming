#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
let mul = 0;
const mylist = list.map(x => x * mul++);
console.log(mylist);
