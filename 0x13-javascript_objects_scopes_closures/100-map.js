#!/usr/bin/node
/*
a script that imports an array and computes a new array
*/
const list = require('./100-data.js').list;
console.log(list);
const arr = list.map((x, index) => x * index);
console.log(arr);
