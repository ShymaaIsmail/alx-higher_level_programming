#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const newList = list.map(function (index, element) {
  return index * element;
});
console.log(newList)
;
