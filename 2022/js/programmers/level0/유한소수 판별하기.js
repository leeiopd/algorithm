function solution(a, b) {
  var answer = 0;

  let i = 2;
  while (i <= b) {
    if (b % i || a % i) {
      i++;
      continue;
    }
    a /= i;
    b /= i;
  }

  while (b % 2 === 0) b /= 2;

  while (b % 5 === 0) b /= 5;

  return b === 1 ? 1 : 2;
}
