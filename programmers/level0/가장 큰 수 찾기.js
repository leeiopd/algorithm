function solution(array) {
  const sorted = array.map((item) => item).sort((a, b) => b - a);
  return [sorted[0], array.indexOf(sorted[0])];
}
