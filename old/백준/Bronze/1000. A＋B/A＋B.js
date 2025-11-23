const fs = require("fs")
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map((i)=>parseInt(i))

console.log(inputs[0]+inputs[1])