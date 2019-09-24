#!/usr/bin/node
/*
a script that prints the title of a Star Wars
movie where the episode number matches a given integer.
*/
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
