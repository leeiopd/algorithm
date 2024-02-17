function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((a, b, _) => (a += parseInt(b)), 0);
}
