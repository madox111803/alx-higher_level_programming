#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Not a number');
} else {
  args.forEach(arg => {
    if (isNaN(parseInt(arg, 10))) {
      console.log('Not a number');
    } else {
      const num = parseInt(arg, 10);
      console.log(`My number: ${num}`);
    }
  });
}

