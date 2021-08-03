#!/usr/bin/node

let idx = 0;
const list = require('./100-data').list;


console.log(list);
const map1 = list.map(x => x * idx++);
console.log(map1);
