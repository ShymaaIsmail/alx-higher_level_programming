#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  let fn = 0;
  if (n === undefined) {
    fn = 1;
  }
  if (n < 0) {
    fn = -1;
  } else if (n === 0) {
    fn = 1;
  } else if (n > 0) {
    fn = n * factorial(n - 1);
  }
  return (fn);
}
console.log(factorial(parseInt(argv[2])));
