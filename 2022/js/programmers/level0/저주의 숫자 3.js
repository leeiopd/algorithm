function solution(n) {
  let answer = 0;
  let count = 0;

  while (count < n) {
    answer++;

    if (answer % 3 === 0 || answer.toString().split("").indexOf("3") !== -1) {
      continue;
    }
    count++;
  }

  return answer;
}
