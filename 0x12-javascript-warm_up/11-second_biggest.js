#!/usr/bin/node

let secondBiggest = 0;
const numbers = [process.argv.slice(2)].flat().sort((a, b) => b - a);
if (numbers[1] !== undefined) {
  secondBiggest = numbers[1];
}
console.log(secondBiggest);
