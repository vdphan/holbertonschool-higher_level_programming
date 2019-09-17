#!/usr/bin/node
/*
a script that prints the addition of 2 integers
*/
function add (a, b) {
  return a + b;
}
const num = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);
if (isNaN(num) && isNaN(num2)) {
  console.log(num);
} else {
  console.log(add(num, num2));
}
