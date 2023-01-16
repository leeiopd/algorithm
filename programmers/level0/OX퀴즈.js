function solution(quiz) {
  var answer = [];
  for (q of quiz) {
    q = q.split(" ");
    const X = parseInt(q[0]);
    const Y = parseInt(q[2]);
    const Z = parseInt(q[4]);
    const result = q[1] === "+" ? X + Y : X - Y;

    if (result === Z) answer.push("O");
    else answer.push("X");
  }
  return answer;
}
