#!/usr/bin/node
/*
a script that concats 2 files
*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
