#!/usr/bin/node
const argv = process.argv;
const len = argv.length;
const arr = [];
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    arr.push(Number(argv[i]));
  }
  arr.sort(function (a, b) {
    return (a - b);
  });
  console.log(arr[arr.length - 2]);
}
