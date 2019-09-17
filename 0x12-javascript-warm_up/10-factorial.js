#!/usr/bin/node
/*
a script that computes and prints a factorial
*/
function fac (num) {
  if (num === 0 | isNaN(num)) {
    return 1;
  } else {
    return num * fac(num - 1);
  }
}
const num = parseInt(process.argv[2], 10);
console.log(fac(num));
