#!/usr/bin/node
const array = process.argv;
let count = 0;
for (let i = 0; array[i]; i++) {
  count += 1;
}
if (count === 2) {
  console.log('No argument');
} else {
  console.log(array[2]);
}
