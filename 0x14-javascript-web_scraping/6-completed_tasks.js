#!/usr/bin/node
/*
a script that computes the number of tasks completed by user id
*/
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  const d = {};
  if (error) {
    console.error('error:', error);
  } else {
    const b = JSON.parse(body);
    for (const u of b) {
      if (u.completed === true) {
        if (!(u.userId in d)) {
          d[u.userId] = 1;
        } else {
          d[u.userId]++;
        }
      }
    }
  }
  console.log(d);
});
