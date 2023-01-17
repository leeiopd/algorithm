function solution(k, m, score) {
  var answer = 0;

  score.sort((a, b) => (a > b ? -1 : 1));

  let i = m - 1;
  while (i < score.length) {
    answer += score[i] * m;
    i += m;
  }
  return answer;
}
