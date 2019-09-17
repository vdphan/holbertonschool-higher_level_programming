#!/usr/bin/node
/*
a script that prints a square
*/
if (process.argv.length === 3) {
  const num = parseInt(process.argv[2], 10);
  if (isNaN(num)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < num; i++) {
      console.log('X'.repeat(num));
    }
  }
} else if (process.argv.length < 3) {
  console.log('Missing size');
}
