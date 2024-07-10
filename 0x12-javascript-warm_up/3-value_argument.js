#!/usr/bin/node
const a = [];
let msg = '';
process.argv.forEach((val) => {
  a.push(`${val}`);
});
if (a.length === 2) {
  msg = 'No argument';
} else {
  msg = a[2];
}
console.log(msg);
