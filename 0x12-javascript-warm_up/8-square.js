#!/usr/bin/node

const mystring = parseInt(process.argv[2]);

if (Number.isInteger(mystring) === Number.isInteger(false)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < mystring; i++) {
        console.log('X'.repeat(mystring));
    }         
}
