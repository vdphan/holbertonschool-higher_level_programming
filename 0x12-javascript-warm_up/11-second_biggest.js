#!/usr/bin/node
/*
a script that searches the second biggest integer in the list of arguments
*/
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(process.argv[i]);
  }
  const arr1 = array.sort(function (a, b) { return b - a; });
  console.log(arr1[1]);
}
