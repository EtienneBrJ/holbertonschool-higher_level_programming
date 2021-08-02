#!/usr/bin/node

const mystring = parseInt(process.argv[2]);

if (Number.isInteger(mystring) === Number.isInteger(false)) {
  console.log('Missing number of occurences');
} else {
    for (let i = 0; i < mystring; i++) {
        console.log('C is fun');
    }
}
