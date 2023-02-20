function solution(k, d) {
  var answer = 0;

  for (let y = 0; y <= d; y += k) {
    answer += parseInt(Math.floor(Math.sqrt(d * d - y * y)) / k) + 1;
  }
  return answer;
}
