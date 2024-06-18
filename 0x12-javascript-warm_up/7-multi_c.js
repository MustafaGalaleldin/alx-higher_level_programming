#!/usr/bin/node
const argv = process.argv;
if (argv.length === 3) {
  const times = Number(argv[2]);
  if (!times) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < times; i++) {
      console.log('C is fu');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
