function solution(n) {
  var answer = new Set();
  const maps = new Array(n).fill(0);
  var answer = 0;

  const dfs = (index, maps) => {
    if (index === n) {
      answer++;
      return;
    }

    for (let i = 1; i <= n; i++) {
      if (maps.indexOf(i) > -1) continue;
      let flag = true;
      for (let j = 1; j <= n; j++) {
        if (index - j < 0) break;
        if (i - j < 1) break;
        if (maps[index - j] === i - j) {
          flag = false;
          break;
        }
      }
      if (!flag) continue;
      for (let j = 1; j <= n; j++) {
        if (index - j < 0) break;
        if (i + j > n) break;
        if (maps[index - j] === i + j) {
          flag = false;
          break;
        }
      }
      if (!flag) continue;
      maps[index] = i;
      dfs(index + 1, maps);
      maps[index] = 0;
    }
  };

  dfs(0, maps);
  return answer;
}

solution(4);
