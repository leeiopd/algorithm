function solution(array) {
  const memo = {};

  for (n of array) {
    if (memo[n]) memo[n]++;
    else memo[n] = 1;
  }

  const max = [-1, -1];
  for (key in memo) {
    if (memo[key] > max[1]) {
      max[0] = key;
      max[1] = memo[key];
    }
  }

  let cnt = 0;
  for (key in memo) {
    if (memo[key] === max[1]) {
      cnt++;
    }
    if (cnt > 1) {
      return -1;
    }
  }

  return parseInt(max[0]);
}
