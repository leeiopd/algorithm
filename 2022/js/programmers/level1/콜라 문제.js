function solution(a, b, n) {
  var answer = 0;
  while (n >= a) {
    n -= a;
    n += b;
    answer += b;
  }

  return answer;
}
