#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
fs.readFile(fileA, 'utf8', (err, data1) => {
  if (err) {
    console.error('Error reading file1:', err);
    return;
  }

  // Read content of file2
  fs.readFile(fileB, 'utf8', (err, data2) => {
    if (err) {
      console.error('Error reading file2:', err);
      return;
    }

    // Combine content of file1 and file2
    const combinedContent = data1 + data2;

    // Write combined content to a new file
    fs.writeFile(fileC, combinedContent, (err) => {
      if (err) {

      }
    });
  });
});
