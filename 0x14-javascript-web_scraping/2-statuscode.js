#!/usr/bin/node
const http = require('request');
http(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('Code: ' + response.statusCode);
});
