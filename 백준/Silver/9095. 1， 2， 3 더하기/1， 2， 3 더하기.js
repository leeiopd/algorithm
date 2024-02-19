const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n").map((n)=>+n);

const N = inputs.shift()

const list = new Array(12).fill(0)

list[1] = 1
list[2] = 2
list[3] = 4

for(let i = 4; i < 12; i++){
    list[i] = list[i-1] + list[i-2] + list[i-3]
}

for(input of inputs){
    console.log(list[input])
}

