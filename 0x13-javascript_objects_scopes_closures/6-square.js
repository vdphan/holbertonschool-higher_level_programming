#!/usr/bin/node
/*
a class Square that defines a square
and inherits from Square of 5-square.js:
*/
const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    let a;
    if (c) {
      a = c;
    } else {
      a = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(a.repeat(this.width));
    }
  }
};
