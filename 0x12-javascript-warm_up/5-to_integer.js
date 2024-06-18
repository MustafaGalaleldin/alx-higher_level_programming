#!/usr/bin/node
const array = process.argv;
if (array.length === 3) {
  const number = Number(array[2]);
  if (!number) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${number}`);
  }
}
