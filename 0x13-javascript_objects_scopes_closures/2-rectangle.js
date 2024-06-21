#!/usr/bin/node
/*
This module contains a Rectangle class.
Instance attribute width is initialized with the value of w.
Instance attribute height is initializes with the value h.
if w or h is equal to 0 or not a positive integer an empty object is created.
*/
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
