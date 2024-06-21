#!/usr/bin/node
/*
This module contains a function that increments and calls a function.
  the function is visible from outside.
*/
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
