#!/usr/bin/node

int1 = parseInt(process.argv[2]);
int2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(int1, int2);
