function solution(num_list, n) {
  let tmp = [];
  const answer = [];
  for (let i = 1; i <= num_list.length; i++) {
    tmp.push(num_list[i - 1]);
    if (i % n) continue;
    answer.push(tmp);
    tmp = [];
  }
  return answer;
}
