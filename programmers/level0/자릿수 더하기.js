function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((acc, cur, idx) => (acc += parseInt(cur)), 0);
}
