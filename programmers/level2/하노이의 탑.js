function solution(n) {
  const dfs = (n, from, through, to) => {
    if (n === 1) return [[from, to]];

    let tmp = [];
    tmp = tmp.concat(dfs(n - 1, from, to, through));
    tmp.push([from, to]);
    tmp = tmp.concat(dfs(n - 1, through, from, to));

    return tmp;
  };

  const answer = dfs(n, 1, 2, 3);

  return answer;
}
