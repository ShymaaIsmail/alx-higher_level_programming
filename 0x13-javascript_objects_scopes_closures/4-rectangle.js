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

  rotate () {
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
