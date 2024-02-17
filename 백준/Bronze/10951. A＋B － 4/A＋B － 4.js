const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (input of inputs){
    input = input.split(" ").map((n)=>parseInt(n))
    console.log(input[0]+input[1])
}
