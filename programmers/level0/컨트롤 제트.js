function solution(s) {
  var answer = 0;
  let tmp = "";

  for (item of s.split(" ")) {
    if (item === "Z") {
      answer -= parseInt(tmp);
      tmp = "";
      continue;
    }

    answer += parseInt(item);
    tmp = item;
  }
  return answer;
}
