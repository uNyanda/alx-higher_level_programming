#!/usr/bin/node
/*
 This script searches the second biggest integer in the list of arguments.
  all arguments can be converted to integers.
  if no arguments are passed, it prints 0.
  if the number of arguments is 1, it prints 1.
*/
const { argv } = require('node:process');

let largest = Number.NEGATIVE_INFINITY;
let secondLargest = Number.NEGATIVE_INFINITY;

for (let i = 2; i < argv.length; i++) {
  const num = Number(argv[i]);
  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest && num !== largest) {
    secondLargest = num;
  }
}

if (argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondLargest);
}
