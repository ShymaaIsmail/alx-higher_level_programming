#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  let square = '';
  for (let row = 0; row < num; row++) {
    for (let col = 0; col < num; col++) {
      square += 'X';
    }
    if (row < num - 1) {
      square += '\n';
    }
  }
  if (square.length > 0) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
