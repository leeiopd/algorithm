const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  const N = Number(input[0]);
  const STAR = "*";
  for (let i = 1; i < N + 1; i++) {
    console.log(STAR.repeat(i));
  }
});
