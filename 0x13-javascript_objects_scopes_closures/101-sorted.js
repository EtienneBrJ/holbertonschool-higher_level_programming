#!/usr/bin/node

const d = require('./101-data').dict;
const nDict = {};

for (const key in d) {
  if (typeof (nDict[d[key]]) === 'undefined') {
    nDict[d[key]] = [];
  }
  nDict[d[key]].push(key);
}
console.log(nDict);
