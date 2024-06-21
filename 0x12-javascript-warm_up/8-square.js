#!/usr/bin/node
/*
 This script prints a square.
   the first argument is the size of the square
   if the first argument can't be converted to an integer, it prints "Missing size"
   the character 'x' is used to print the square.
*/
const { argv } = require('node:process');

// function checks if the argument is a integer
function isInteger (arg) {
  const number = Number(arg);
  return !isNaN(number) && Number.isInteger(number);
}

const firstArg = argv[2];
const squareChar = 'X';

if (!isInteger(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    console.log(squareChar.repeat(firstArg));
  }
}
