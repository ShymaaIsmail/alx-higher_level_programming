#!/usr/bin/node
const http = require('request');
http.get(process.argv[2], function (error, response) {
  if (error) { console.log(error); }
  console.log('Code: ' + response.statusCode);
});
