#!/usr/bin/node

const SquareX = require('./5-square').Square;

function Square (size) {
  SquareX.call(this, size);
  this.size = size;

  Square.prototype.charPrint = function (c) {
	  if (c === undefined) {
		  c = 'X';
	  }

	  for (let i = 0; i < this.size; i++) {
		  console.log(c.repeat(this.size));
	  }
  };
}

exports.Square = Square;
