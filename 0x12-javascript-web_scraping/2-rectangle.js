#!/usr/bin/node

function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
};

exports.Rectangle = Rectangle;
