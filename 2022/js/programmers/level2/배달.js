function solution(N, road, K) {
  var answer = 0;

  const roadTmp = new Array(N + 1).fill(0);

  const map = [];
  for (let i = 0; i <= N; i++) {
    map[i] = [...roadTmp];
  }

  for (r of road) {
    if (!map[r[0]][r[1]] || !map[r[1]][r[0]]) {
      map[r[0]][r[1]] = r[2];
      map[r[1]][r[0]] = r[2];
      continue;
    }

    map[r[0]][r[1]] = map[r[0]][r[1]] < r[2] ? map[r[0]][r[1]] : r[2];
    map[r[1]][r[0]] = map[r[1]][r[0]] < r[2] ? map[r[1]][r[0]] : r[2];
  }

  const shortCut = new Array(N + 1).fill(500001);

  shortCut[0] = 500001;
  shortCut[1] = 0;

  const queue = [1];

  while (queue.length) {
    const now = queue[0];
    queue.shift();

    for (let i = 1; i <= N; i++) {
      if (!map[now][i]) continue;
      if (shortCut[now] + map[now][i] > K) continue;
      if (shortCut[now] + map[now][i] <= shortCut[i]) {
        shortCut[i] = shortCut[now] + map[now][i];
        queue.push(i);
      }
    }
  }

  for (s of shortCut) {
    if (!s) continue;
    if (s > K) continue;
    answer++;
  }

  return answer + 1;
}
