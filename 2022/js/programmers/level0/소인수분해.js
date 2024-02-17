function solution(n) {
  var answer = [];
  let k = 2;

  while (n > 1) {
    if (n % k) {
      k += 1;
      continue;
    }

    n /= k;
    if (answer.indexOf(k) === -1) answer.push(k);
  }
  return answer;
}
