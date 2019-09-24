#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myx = '';
    for (let i = 0; i < this.width; i++) {
      console.log(myx.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
