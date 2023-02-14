function solution(x, y, n) {
  var answer = 10000000;

  const queue = [y];
  const memo = new Array(10000001).fill(0);

  while (queue.length) {
    const q = queue[0];
    queue.shift();

    if (q === x) {
      if (answer > memo[x]) {
        answer = memo[x];
      }
    }

    if (q - n >= x && !memo[q - n]) {
      memo[q - n] = memo[q] + 1;
      queue.push(q - n);
    }
    if (q % 2 === 0 && q / 2 >= x && !memo[q / 2]) {
      memo[q / 2] = memo[q] + 1;
      queue.push(q / 2);
    }
    if (q % 3 === 0 && q / 3 >= x && !memo[q / 3]) {
      memo[q / 3] = memo[q] + 1;
      queue.push(q / 3);
    }
  }

  return answer === 10000000 ? -1 : answer;
}
