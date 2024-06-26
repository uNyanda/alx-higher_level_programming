#!/usr/bin/node
/*
This module contains a function that returns the number of occurrences in a list.
*/
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
