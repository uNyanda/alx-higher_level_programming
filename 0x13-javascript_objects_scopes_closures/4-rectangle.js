#!/usr/bin/node
/*
This module contains a Rectangle class.
  the width attribute is initialized with the value w.
  the height attribute is initialized with the value h.
  if w or h is equal to 0 or not an integer, an empty object is created.
  Instance method print() prints the rectangle using the character X.
  Instance method rotate() that exchanges the width and the height of the rectangle.
  Instance method double() that multiples the width and the height of the rectangle by 2.
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
