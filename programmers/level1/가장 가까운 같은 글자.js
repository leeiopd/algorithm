function solution(s) {
  var answer = [];
  const tmp = {};

  for (let i = 0; i < s.length; i++) {
    if (!tmp[s[i]]) {
      answer.push(-1);
    } else {
      answer.push(i - tmp[s[i]] + 1);
    }

    tmp[s[i]] = i + 1;
  }
  return answer;
}
