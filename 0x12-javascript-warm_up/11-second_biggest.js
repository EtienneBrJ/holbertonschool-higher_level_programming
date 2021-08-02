#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const arr = argv.slice(2).map(Number);
  const max2 = arr.sort(function (a, b) { return b - a; })[1];
  console.log(max2);
}
