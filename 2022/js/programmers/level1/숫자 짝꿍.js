function solution(X, Y) {
  const x_list = new Array(10).fill(0);
  const y_list = new Array(10).fill(0);

  X.split("").forEach((i) => x_list[parseInt(i)]++);
  Y.split("").forEach((i) => y_list[parseInt(i)]++);

  const count = new Array(10).fill(0);
  for (let i = 0; i <= 10; i++) {
    while (x_list[i] && y_list[i]) {
      count[i]++;
      x_list[i]--;
      y_list[i]--;
    }
  }

  let answer = "";
  for (let i = 9; i > 0; i--) {
    for (let j = 0; j < count[i]; j++) {
      answer += i.toString();
    }
  }

  if (answer.length && count[0]) {
    for (let i = 0; i < count[0]; i++) {
      answer += "0";
    }
  }
  if (!answer.length && count[0]) answer = "0";
  return answer.length ? answer : "-1";
}
