#!/usr/bin/node
/*
This module contains a function that converts a number from base 10 to another base passed as argument.
*/
exports.converter = function (base) {
  function convert (number) {
    return base === 16
      ? number.toString(16)
      : base === 10
        ? number.toString(10)
        : base === 8
          ? number.toString(8)
          : base === 2
            ? number.toString(2)
            : base.toString();
  }
  return convert;
};
