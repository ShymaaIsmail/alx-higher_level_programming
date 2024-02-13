#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let index = 0; index < this.height; index++) {
      for (let index = 0; index < this.width; index++) {
        rect += 'X';
      }
      if (index < this.height - 1) {
        rect += '\n';
      }
    }
    if (rect.length > 0) {
      console.log(rect);
    }
  }
}
module.exports = Rectangle;
