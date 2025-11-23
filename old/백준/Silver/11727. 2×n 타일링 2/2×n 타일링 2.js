const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

const N = +inputs.shift()

const tile = new Array(N+1).fill(0)

tile[0] = 1
tile[1] = 1
tile[2] = 3

for (let i = 3; i <= N; i++){
    tile[i] = (tile[i-1] + (tile[i-2]*2)) % 10007
}

console.log(tile[N])