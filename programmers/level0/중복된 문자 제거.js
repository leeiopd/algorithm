function solution(my_string) {
  var answer = [];
  my_string.split("").forEach((str) => {
    if (answer.indexOf(str) === -1) answer.push(str);
  });
  return answer.join("");
}
