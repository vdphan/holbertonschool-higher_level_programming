#!/usr/bin/node
/*
a function that prints the number of arguments
already printed and the new argument value
*/
var c = 0;
exports.logMe = function (item) {
  console.log(`${c}: ${item}`);
  c++;
};
