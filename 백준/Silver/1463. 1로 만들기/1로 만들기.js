const fs = require("fs")
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim())

/*
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
*/

const MIN = 100000000;

const memory = new Array(10).fill(100000000);

const dfs = (n, time = 0) => {
    if (memory[n] < time) return;

    memory[n] = time;

    if (n === 1) {
        return;
    }

    if (n % 3 === 0) dfs(parseInt(n / 3), time + 1);
    if (n % 2 === 0) dfs(parseInt(n / 2), time + 1);
    dfs(n - 1, time + 1);
};

dfs(input);

console.log(memory[1]);