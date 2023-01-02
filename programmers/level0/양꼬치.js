function solution(n, k) {
  let free = parseInt(n / 10);
  return n * 12000 + (k - free) * 2000;
}
