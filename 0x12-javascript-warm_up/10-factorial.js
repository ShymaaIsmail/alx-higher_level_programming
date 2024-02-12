#!/usr/bin/node
function factorial (n) {
  let fn = 0;
  if (n < 0) {
    fn = -1;
  } else if (n === 0 || n === undefined || isNaN(n)) {
    fn = 1;
  } else if (n > 0) {
    fn = n * factorial(n - 1);
  }
  return (fn);
}
console.log(factorial(Number(process.argv[2])));
