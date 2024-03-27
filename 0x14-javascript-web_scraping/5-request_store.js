#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error fetching the webpage:', error);
    return;
  }

  // Write the body content to the file
  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      console.error('Error writing to file:', err);
    }
  });
});
