#!/usr/bin/node
const { argv } = require('node:process');

const num = parseInt(argv[2]);

if (!isNaN(num)) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}
