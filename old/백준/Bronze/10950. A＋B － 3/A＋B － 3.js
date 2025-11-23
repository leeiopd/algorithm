const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (let i = 1; i <= parseInt(inputs[0]); i++) {
    const [a, b] = inputs[i].split(" ").map((n) => parseInt(n));

    console.log(a + b);
}
