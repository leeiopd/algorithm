function solution(k, dungeons) {
  var answer = -1;

  const DFS = (k, dungeons, depth, memo) => {
    if (depth > dungeons.length) {
      return;
    }
    if (depth > answer) {
      answer = depth;
    }

    for (let i = 0; i < dungeons.length; i++) {
      if (memo.indexOf(i) > -1) {
        continue;
      }

      if (k < dungeons[i][0]) continue;

      DFS(k - dungeons[i][1], dungeons, depth + 1, [...memo, i]);
    }
  };

  for (let i = 0; i < dungeons.length; i++) {
    DFS(k - dungeons[i][1], dungeons, 1, [i]);
  }

  return answer;
}
