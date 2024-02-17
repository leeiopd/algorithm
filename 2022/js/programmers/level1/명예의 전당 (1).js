function solution(k, score) {
  var answer = [];
  const list = [];

  for (let i = 0; i < score.length; i++) {
    if (list.length < k) {
      list.push(score[i]);
      list.sort((a, b) => (a > b ? -1 : 1));
    } else {
      if (list[list.length - 1] < score[i]) {
        list.pop();
        list.push(score[i]);
        list.sort((a, b) => (a > b ? -1 : 1));
      }
    }
    answer.push(list[list.length - 1]);
  }

  return answer;
}
