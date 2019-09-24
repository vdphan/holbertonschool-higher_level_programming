#!/usr/bin/node
/*
a script that prints the number of movies where the character “Wedge Antilles” is present
*/
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  let c = 0;
  if (error) {
    console.error('error:', error);
  } else {
    const b = JSON.parse(body);
    for (const item of b.results) {
      if (item.characters.includes('https://swapi.co/api/people/18/')) {
        c++;
      }
    }
    console.log(c);
  }
});
