function solution(n, wires) {
  var answer = 999999999;
  const maps = [];

  for (let i = 0; i <= n; i++) {
    maps[i] = new Array(n + 1).fill(0);
  }

  for (w of wires) {
    maps[w[0]][w[1]] = 1;
    maps[w[1]][w[0]] = 1;
  }

  for (w of wires) {
    maps[w[0]][w[1]] = 0;
    maps[w[1]][w[0]] = 0;

    const dist = new Array(n + 1).fill(0);
    let count = 0;
    const dfs = (from) => {
      if (dist[from]) return;
      count++;
      dist[from] = 1;
      for (let i = 1; i <= n; i++) {
        if (i === from) continue;
        if (maps[from][i]) {
          dfs(i);
        }
      }
    };

    dfs(1);

    if (answer > Math.abs(n - 2 * count)) answer = Math.abs(n - 2 * count);

    maps[w[0]][w[1]] = 1;
    maps[w[1]][w[0]] = 1;
  }
  return answer;
}
