function solution(my_string) {
  let answer = 0;
  let tmp = "";

  for (str of my_string) {
    if (!isNaN(str)) {
      tmp += str;
      continue;
    }
    if (tmp) answer += parseInt(tmp);
    tmp = "";
  }
  return tmp.length ? answer + parseInt(tmp) : answer;
}
