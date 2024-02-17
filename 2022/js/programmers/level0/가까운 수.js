function solution(array, n) {
  array.sort();
  var answer = 0;
  let min = 9999999;
  for (i of array) {
    if (Math.abs(n - i) < min) {
      min = Math.abs(n - i);
      answer = i;
    }
  }
  return answer;
}
