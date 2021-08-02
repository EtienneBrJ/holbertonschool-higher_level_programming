#!/usr/bin/node

if (process.argv[2] == null || process.argv[3] == null) {
  console.log('No argument');
} else if (process.argv[3] == null) {
  console.log(process.argv[2]);
}
