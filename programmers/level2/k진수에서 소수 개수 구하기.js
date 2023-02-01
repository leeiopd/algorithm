function solution(n, k) {
  var answer = 0;

  const nNumber = n
    .toString(k)
    .split("0")
    .map((i) => {
      if (i.length) return parseInt(i);
    });

  for (i of nNumber) {
    if (parseInt(i) > 1) {
      const tmp = parseInt(i);
      let flag = true;
      for (let j = 2; j <= Math.sqrt(tmp); j++) {
        if (tmp % j === 0) {
          flag = false;
          break;
        }
      }

      if (flag) answer++;
    }
  }

  return answer;
}
