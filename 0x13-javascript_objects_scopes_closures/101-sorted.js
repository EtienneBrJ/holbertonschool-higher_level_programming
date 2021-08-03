#!/usr/bin/node

const d = require('./101-data').dict;
const new_dict = {};

for (const key in d) {
    if (typeof (new_dict[d[key]]) === 'undefined') {
        new_dict[d[key]] = [];
    }
    new_dict[d[key]].push(key);
}
console.log(new_dict);