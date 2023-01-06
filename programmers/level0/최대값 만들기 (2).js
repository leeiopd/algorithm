function solution(numbers) {
  const sorted = numbers.sort((a, b) => a - b);
  return sorted[0] * sorted[1] >
    sorted[numbers.length - 1] * sorted[numbers.length - 2]
    ? sorted[0] * sorted[1]
    : sorted[numbers.length - 1] * sorted[numbers.length - 2];
}
