#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return Array(list).flat().filter(a => a === searchElement).length;
};
