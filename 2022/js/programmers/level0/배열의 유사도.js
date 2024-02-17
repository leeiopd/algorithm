function solution(s1, s2) {
  var answer = 0;
  s1.forEach((i) => {
    if (s2.indexOf(i) > -1) answer++;
  });

  return answer;
}
