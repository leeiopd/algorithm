function solution(array, n) {
  let answer = 0;
  array.map((item) => (item === n ? answer++ : null));
  return answer;
}
