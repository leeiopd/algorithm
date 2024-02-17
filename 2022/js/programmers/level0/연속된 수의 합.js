function solution(num, total) {
  var answer = [];

  let min = -50;
  let max = -50 + num - 1;
  let adds = 0;

  for (let i = min; i <= max; i++) {
    adds += i;
  }

  while (max <= 1000) {
    if (adds === total) break;
    adds -= min;
    max++;
    min++;
    adds += max;
  }

  for (let i = min; i <= max; i++) {
    answer.push(i);
  }

  return answer;
}
