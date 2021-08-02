#!/usr/bin/node

const argv = process.argv;
const arg1 = parseInt(argv[2]);

function fact (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

if (isNaN(arg1)) {
  console.log(1);
} else {
  console.log(fact(arg1));
}
