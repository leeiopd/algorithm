function solution(emergency) {
  return emergency.map(
    (n) => [...emergency].sort((a, b) => b - a).indexOf(n) + 1
  );
}
