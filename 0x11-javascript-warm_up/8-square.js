#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}

let printer = '';
for (let col = 0; col < process.argv[2]; col++) {
  for (let row = 0; row < process.argv[2]; row++) {
    printer += 'X';
  }
  console.log(printer);
  printer = '';
}
