function solution(array) {
  var answer = 0;

  for (n of array) {
    n.toString()
      .split("")
      .forEach((i) => (i === "7" ? answer++ : null));
  }
  return answer;
}
