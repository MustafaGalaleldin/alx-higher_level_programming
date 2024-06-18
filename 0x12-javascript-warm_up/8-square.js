#!/usr/bin/env node
const argv = process.argv;
if (argv.length === 3) {
  const size = Number(argv[2]);
  if (!size) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
} else {
  console.log('Missing size');
}
