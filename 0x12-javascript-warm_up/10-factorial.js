#!/usr/bin/node

const int_arg1 = parseInt(process.argv[2]);

function fact (num) {
  if (num === 0) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

if (isNaN(int_arg1)) {
    console.log(1);
} else {
    console.log(fact(int_arg1));
}

