#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  if (list) {
    for (let index = list.length - 1; index >= 0; index--) {
      const element = list[index];
      revList.push(element);
    }
  }
  return revList;
};
