#!/usr/bin/node
/*
 This script prints a message depending of the number of arguments passed:
   if no arguments are passed to the script, it prints "No argument"
   if only one argument is passed to the script, it prints "Argument found"
   otherwise, it prints "Arguments found"
 */
const { argv } = require('node:process');

if (argv.length <= 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
