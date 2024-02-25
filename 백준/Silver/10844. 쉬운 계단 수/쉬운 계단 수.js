const fs = require("fs")
const N = +fs.readFileSync("/dev/stdin").toString().trim()

const list = new Array(N + 1);

for (let i = 0; i < N + 1; i++) {
    list[i] = new Array(10).fill(0);
}

for (let i = 1; i < 10; i++) {
    list[1][i] = 1;
}

//   0 1 2 3 4 5 6 7 8 9
// 1 0 1 1 1 1 1 1 1 1 1
// 2 1 1 2 2 2 2 2 2 2 1
// 3 1 3 3 4 4 4 4 4 3 2

for (let i = 2; i <= N; i++) {
    list[i][0] = list[i - 1][1] % 1000000000;
    list[i][9] = list[i - 1][8] % 1000000000;
    for (let j = 1; j < 9; j++) {
        list[i][j] = (list[i - 1][j - 1] + list[i - 1][j + 1]);
        list[i][j] %= 1000000000
    }
}

let answer = 0;

for (let i = 0; i < 10; i++) {
    answer = (answer +list[N][i]) % 1000000000;
}

console.log(answer % 1000000000);