#!/usr/bin/node
const array = process.argv;
let count = 0;
for (let i = 0; array[i]; i++) {
  count += 1;
}
if (count === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < count; i++) {
    console.log(array[i]);
  }
}
