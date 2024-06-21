#!/usr/bin/node
/*
This module contains a class Square that inherits from Square of 5-square.js.
  Instance method charPrint(c) that prints the rectangle using the character C.
    if C is undefined, it uses the character X.
*/

const Squares = require('./5-square');

class Square extends Squares {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    // if c is undefined, use 'X' as the default character
    const character = c || 'X';

    // create a row with the specified character
    const row = character.repeat(this.width);

    // Print the row for each height
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Square;
