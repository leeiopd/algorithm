function solution(my_str, n) {
  var answer = [];
  let tmp = "";
  for (str of my_str) {
    tmp += str;
    if (tmp.length === n) {
      answer.push(tmp);
      tmp = "";
    }
  }
  if (tmp) answer.push(tmp);
  return answer;
}
