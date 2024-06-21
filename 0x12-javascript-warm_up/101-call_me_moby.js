#!/usr/bin/node
/*
This function executes x times a function.
  it is visible from outside.
*/
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
