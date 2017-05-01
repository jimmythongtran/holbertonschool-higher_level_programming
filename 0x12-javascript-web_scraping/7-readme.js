#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, info) => {
  if (error) {
    return console.log(error);
  } else {
    console.log(info.trim());
  }
});
