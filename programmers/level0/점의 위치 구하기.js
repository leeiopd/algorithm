function solution(dot) {
  const [X, Y] = dot;

  return X * Y > 0 ? (X > 0 ? 1 : 3) : X > 0 ? 4 : 2;
}
