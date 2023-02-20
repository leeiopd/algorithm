function solution(storey) {
  var answer = 0;

  storey = storey
    .toString()
    .split("")
    .reverse()
    .map((i) => parseInt(i));

  let tmp = 0;

  for (let i = 0; i < storey.length; i++) {
    let n = storey[i];
    if (tmp > 0) {
      n++;
      tmp = 0;
    }

    if (n === 5) {
      answer += 5;
      if (storey[i + 1] >= 5) {
        tmp = 1;
      }
    }

    if (n < 5) {
      answer += n;
    }
    if (n > 5) {
      answer += 10 - n;
      tmp = 1;
    }
  }

  return answer + tmp;
}
