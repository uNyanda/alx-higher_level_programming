#!/usr/bin/node
/*
 This script prints x times 'C is fun'
 x is the first argument of the script
 if the first argument can't be converted to an integer, it prints "Missing number of occurences"
*/
const { argv } = require('node:process');

const myVar = 'C is fun';

// function to check if argument is a integer
function isInteger (arg) {
  const number = Number(arg);
  return !isNaN(number) && Number.isInteger(number);
}

const firstArg = argv[2];
let i;

if (!isInteger(firstArg)) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < firstArg; i++) {
    console.log(myVar);
  }
}
