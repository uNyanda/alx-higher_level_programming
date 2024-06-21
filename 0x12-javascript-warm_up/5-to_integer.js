#!/usr/bin/node
/*
 This script prints "My number: <first argument converted in integer>"
   if the first argument can be converted to an integer.
   if the argument can't be converted to an integer, it prints "Not a number".
 */
const { argv } = require('node:process');

// function to check if an argument is a number
function isNumber (arg) {
  const number = Number(arg);
  return !isNaN(number);
}

// get the first argument
const firstArg = argv[2];

// check if the first argument can be converted to a number
if (isNumber(firstArg)) {
  console.log('My number: ' + parseInt(parseFloat((firstArg))));
} else {
  console.log('Not a number');
}
