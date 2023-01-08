function solution(balls, share) {
  var answer = 1;

  for (let i = share + 1; i <= balls; i++) {
    answer *= i;
  }
  for (let i = 2; i <= balls - share; i++) {
    answer /= i;
  }

  return parseInt(answer);
}
