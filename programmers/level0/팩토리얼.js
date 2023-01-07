function solution(n) {
  let tmp = 1;

  for (let i = 2; i <= 10; i++) {
    tmp *= i;
    if (n === tmp) return i;
    if (n < tmp) return i - 1;
  }
}
