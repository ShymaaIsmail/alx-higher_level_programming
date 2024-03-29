#!/usr/bin/node
const http = require('request');
const url = process.argv[2];
http.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const result = JSON.parse(body);
  const movies = result.results.filter(a => {
    return a.characters.some(character => character.endsWith('/18/'));
  });
  console.log(movies.length);
});
