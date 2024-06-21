#!/usr/bin/node
/*
This module contains a function that prints the number of arguments already printed and the new
argument value.
*/
exports.logMe = function (item) {
  if (!exports.logMe.counter) {
    exports.logMe.counter = 0;
  }
  console.log(`${exports.logMe.counter}: ${item}`);
  exports.logMe.counter++;
};
