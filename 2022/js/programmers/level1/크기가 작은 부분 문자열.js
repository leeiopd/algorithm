function solution(t, p) {
  var answer = 0;

  for (let i = 0; i <= t.length - p.length; i++) {
    const num = t.slice(i, i + p.length);
    if (parseInt(num) <= parseInt(p)) {
      answer++;
    }
  }
  return answer;
}
