#!/usr/bin/node

/*
This module contains a script that imports an array and computes a new array.
  * it imports list from the file 100-data.js *
The new list is created with each value equal to the value of the initial list, multiplied by the index in the list.
 both the initial list and the new list are printed.
*/
const oldlist = require('./100-data').list;

const newlist = oldlist.map((value, index) => value * index);

console.log(oldlist);
console.log(newlist);
