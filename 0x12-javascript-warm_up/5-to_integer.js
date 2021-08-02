#!/usr/bin/node

const mystring = parseInt(process.argv[2]);

if (Number.isInteger(mystring) === Number.isInteger(false)) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + mystring);
}
