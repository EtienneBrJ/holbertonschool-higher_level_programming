#!/usr/bin/node

const argv = process.argv;
let max; let max2 = 0;

if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    if (i === 2) {
      max = parseInt(argv[i]);
      max2 = parseInt(argv[i]);
      continue;
    }
    if (parseInt(argv[i]) > max) {
      max2 = max;
      max = parseInt(argv[i]);
    }
  }
  console.log(max2);
}
