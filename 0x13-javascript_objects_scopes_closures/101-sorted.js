#!/usr/bin/node
/*
a script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence.
*/
const dict = require('./101-data.js').dict;
const d = {};
for (const [key, value] of Object.entries(dict)) {
  if (!(value in d)) {
    d[value] = [key];
  } else {
    d[value].push(key);
  }
}
console.log(d);
