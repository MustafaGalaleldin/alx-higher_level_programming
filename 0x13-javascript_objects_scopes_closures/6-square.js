#!/usr/bin/node
const PSquare = require('./5-square');
class Square extends PSquare {
  charPrint (c) {
    let shape;
    if (!c) {
      shape = 'X';
    } else {
      shape = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(shape.repeat(this.width));
    }
  }
}
module.exports = Square;
