#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myx = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(myx.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
