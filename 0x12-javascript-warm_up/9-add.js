#!/usr/bin/node
/*
 This script prints the addition of 2 integers.
   the first argument is the first integer.
   the second argument is the second integer.
*/
const { argv } = require('node:process');

const firstArg = argv[2];
const secondArg = argv[3];

// function adds two integers.
function addition (a, b) {
  return Number(a) + Number(b);
}

if (argv.length !== 4 || isNaN(firstArg) || isNaN(secondArg)) {
  console.log(NaN);
} else {
  const result = addition(firstArg, secondArg);
  console.log(result);
}
