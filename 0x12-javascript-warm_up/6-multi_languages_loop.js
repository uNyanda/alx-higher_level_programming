#!/usr/bin/node
/*
 This script prints 3 lines but by using an array of strings and a loop
   The first line: "C is fun"
   The second line: "Python is cool"
   The third line: "JavaScript is amazing"
*/
const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let i;

for (i = 0; array[i] !== undefined; i++) {
  console.log(array[i]);
}
