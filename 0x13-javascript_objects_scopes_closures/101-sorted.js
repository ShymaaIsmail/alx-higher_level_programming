#!/usr/bin/node
const dict = require('./101-data').dict;

console.log(dict);
const newDict = Object.fromEntries(
  Object.entries(dict).map(([key, value]) => {
    return [
      value,
      Object.entries(dict).filter(([k, val]) => val === value)
        .map(([key, val]) => key)
    ];
  }
  ));
console.log(newDict);
