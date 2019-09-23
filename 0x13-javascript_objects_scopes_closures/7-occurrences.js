#!/usr/bin/node
/*
a function that returns the number of occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const num of list) {
    if (num === searchElement) {
      c++;
    }
  }
  return c;
};
