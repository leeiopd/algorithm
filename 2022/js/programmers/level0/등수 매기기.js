function solution(score) {
  const answer = new Array(score.length).fill(1);

  for (let i = 0; i < score.length; i++) {
    for (let j = 0; j < score.length; j++) {
      if (i === j) continue;

      if (score[i][0] + score[i][1] > score[j][0] + score[j][1]) {
        answer[j]++;
      }
    }
  }
  return answer;
}
