#!/usr/bin/node

let n = parseInt(process.argv[2]);

function Factorial (number) {
  if (number === 0) {
    return 1;
  } if (isNaN(number) === true) {
    return 1;
  }
  return number * Factorial(number - 1);
}
console.log(Factorial(n));
