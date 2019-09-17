#!/usr/bin/node
/*
a script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
if (process.argv.length === 3) {
  const num = parseInt(process.argv[2], 10);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: '.concat(num));
  }
} else {
  console.log('Not a number');
}
