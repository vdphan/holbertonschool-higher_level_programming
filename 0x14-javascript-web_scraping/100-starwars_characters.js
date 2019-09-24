#!/usr/bin/node
/*
a script that prints all characters of a Star Wars movie
*/
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const b1 = JSON.parse(body);
    for (const c of b1.characters) {
      request.get(c, function (e, r, b) {
        if (e) {
          console.error('error:', e);
        } else {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
