#!/usr/bin/node
const argv = process.argv;
let result = 0;
function factorial (n) {
  if (!n || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
result = factorial(Number(argv[2]));
console.log(result);
