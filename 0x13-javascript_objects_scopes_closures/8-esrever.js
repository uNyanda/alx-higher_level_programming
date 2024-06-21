#!/usr/bin/node
/*
This module contains a function that returns the reversed version of a list.
  ** it doesn't use the built-in method 'reverse' **
*/
exports.esrever = function (list) {
  const reversed = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
