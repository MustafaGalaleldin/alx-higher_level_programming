#!/usr/bin/node
const array = process.argv;
const length = array.length;
if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
