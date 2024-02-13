#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (c) {
      let rect = '';
      for (let index = 0; index < this.height; index++) {
        for (let index = 0; index < this.width; index++) {
          rect += c;
        }
        if (index < this.height - 1) {
          rect += '\n';
        }
      }
      if (rect.length > 0) {
        console.log(rect);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
