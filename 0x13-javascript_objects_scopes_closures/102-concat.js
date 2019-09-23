#!/usr/bin/node
/*
a script that concats 2 files
*/
const fs = require('fs');
const a = fs.readFileSync(`./${process.argv[2]}`);
const b = fs.readFileSync(`./${process.argv[3]}`);
fs.appendFileSync(`./${process.argv[4]}`, a + b);
