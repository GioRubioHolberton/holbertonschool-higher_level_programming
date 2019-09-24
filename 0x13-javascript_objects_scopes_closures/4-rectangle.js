#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
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

  rotate () {
    const tem = this.width;
    this.width = this.height;
    this.height = tem;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
