#!/usr/bin/node
/*
This module contains a Square class that inherits from Rectangle.
 the constructor of Rectangle is called (by using super()).
*/

// import the Rectangle class.
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
