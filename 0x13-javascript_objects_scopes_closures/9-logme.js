#!/usr/bin/node
exports.logMe = (function (item) {
  let argNumber = 0;

  return function (item) {
    console.log(argNumber + ': ' + item);
    argNumber++;
  };
})();
