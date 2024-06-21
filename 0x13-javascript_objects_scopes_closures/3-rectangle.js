#!/usr/bin/node
/*
This module contains a Rectangle class.
  the width attribute is initialized with the value w.
  the height attribute is initialized with the value h.
  if w or h is equal to 0 or not an integer, an empty object is created.
  Instance method print() prints the rectangle using the character X.
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
}
module.exports = Rectangle;
