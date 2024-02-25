const fs = require("fs")
const N = parseInt(fs.readFileSync('/dev/stdin').toString().trim())

//   0 1 2 3 4 5 6 7 8 9
// 1 1 1 1 1 1 1 1 1 1 1
// 2 1 2 3 4 5 6 7 8 9 10

const List = [[], new Array(10).fill(1)]

for (let i = 2; i <= N; i++){
    List[i] = new Array(10).fill(0)
    for(let j = 0; j < 10; j++){
        List[i][j] = List[i-1].slice(0, j+1).reduce((acc, cur, idx)=> {return acc+=cur}, 0);
        List[i][j] %= 10007
    }
}

console.log(List[N].reduce((acc, cur, idx)=> {return acc+=cur}, 0) % 10007);

