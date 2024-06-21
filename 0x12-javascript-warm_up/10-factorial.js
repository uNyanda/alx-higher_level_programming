#!/usr/bin/node
/*
 This script computes and prints a factorial.
  factorial of NaN is 1.
*/
const { argv } = require('node:process');

const arg1 = argv[2];

// function computes a factorial of a number.
function factorial (arg) {
  if (arg === 0 || arg === 1 || isNaN(arg)) {
    return 1;
  }
  return arg * factorial(arg - 1);
}

const result = factorial(Number(arg1));
console.log(result);
