#!/usr/bin/node
/*
 This script prints the first argument passed to it:
  if no argument is passed to the script, it prints "No argument"
 */
const { argv } = require('node:process');

let found = false;

for (let i = 2; argv[i] !== undefined; i++) {
  if (!found) {
    console.log(argv[i]);
    found = true;
  }
}
if (!found) {
  console.log('No argument');
}
