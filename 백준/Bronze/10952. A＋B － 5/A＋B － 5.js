const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

for (input of inputs){
    input = input.split(" ").map((n)=>parseInt(n))
    if(input[0] !== 0) console.log(input[0]+input[1])
}
