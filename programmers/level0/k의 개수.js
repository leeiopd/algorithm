function solution(i, j, k) {
  var answer = 0;

  for (let l = i; l <= j; l++) {
    l.toString()
      .split("")
      .forEach((str) => {
        if (parseInt(str) === k) answer++;
      });
  }
  return answer;
}
