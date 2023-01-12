function solution(dots) {
  let max_x = -256;
  let min_x = 256;
  let max_y = -256;
  let min_y = 256;

  for (dot of dots) {
    max_x = dot[0] > max_x ? dot[0] : max_x;
    min_x = dot[0] < min_x ? dot[0] : min_x;
    max_y = dot[1] > max_y ? dot[1] : max_y;
    min_y = dot[1] < min_y ? dot[1] : min_y;
  }

  const len_X = Math.abs(max_x - min_x);
  const len_Y = Math.abs(max_y - min_y);

  return len_X * len_Y;
}
