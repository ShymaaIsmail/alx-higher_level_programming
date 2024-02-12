#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
