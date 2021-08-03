#!/usr/bin/node

const fs = require('fs');

const file1 = fs.readFileSync(process.argv[2], 'utf8');
const file2 = fs.readFileSync(process.argv[3], 'utf8');

const file3 = file1.concat(file2);

fs.writeFile(process.argv[4], file3, 'utf8', function (err, result) { if (err) console.log('error', err); });
