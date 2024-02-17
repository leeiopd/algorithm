function solution(sides) {
  sides.sort((a, b) => a - b);

  const A = sides[0];
  const B = sides[1];

  let answer = 0;

  for (let i = 1; i <= B; i++) {
    answer += A + i > B ? 1 : 0;
  }
  for (let i = B + 1; i < A + B; i++) {
    answer++;
  }

  return answer;
}
