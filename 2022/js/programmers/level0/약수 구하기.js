function solution(n) {
  return Array(n)
    .fill(1)
    .map((_, index) => index + 1)
    .filter((item) => n % item === 0);
}
