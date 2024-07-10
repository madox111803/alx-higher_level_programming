#!/usr/bin/node

const count = process.argv.length;
let arg = ''
if (count === 2) {
	arg = 'No argument';
} else if (count === 3) {
	arg = 'Argument found';
} else {
	arg = 'Arguments found';
}
console.log(arg);
