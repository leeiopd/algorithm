function solution(dots) {
  const a_slope = (dots[0][0] - dots[1][0]) / (dots[0][1] - dots[1][1]);

  const b_slope = (dots[1][0] - dots[2][0]) / (dots[1][1] - dots[2][1]);

  const c_slope = (dots[2][0] - dots[3][0]) / (dots[2][1] - dots[3][1]);

  const d_slope = (dots[3][0] - dots[0][0]) / (dots[3][1] - dots[0][1]);

  if (a_slope === c_slope) return 1;
  if (b_slope === d_slope) return 1;

  return 0;
}
