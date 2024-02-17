function solution(s) {
  var answer = "";

  for (let i = 0; i < s.length; i++) {
    if (s.split(s[i]).length === 2) answer += s[i];
  }
  return answer.split("").sort().join("");
}
