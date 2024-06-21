#!/usr/bin/node
/*
 This script prints two arguments passed to it, in the following format: "is"
 */
const myVar = ' is ';
const { argv } = require('node:process');

const firstArg = argv[2] === undefined ? 'undefined' : argv[2];
const secondArg = argv[3] === undefined ? 'undefined' : argv[3];
const output = firstArg.concat(myVar, secondArg);

console.log(output);
