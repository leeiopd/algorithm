const fs = require("fs")
const input = parseInt(fs.readFileSync("dev/stdin").toString().trim())

const tile = new Array(input+1).fill(0)

tile[1] = 1
tile[2] = 2

for(let i = 3; i <= input; i++){
    tile[i] = (tile[i-1] + tile[i-2]) % 10007
}


console.log(tile[input]);