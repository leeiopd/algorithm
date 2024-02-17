function solution(order) {
  return order
    .toString()
    .split("")
    .reduce(
      (acc, cur, idx) => (acc += parseInt(cur) && !(parseInt(cur) % 3) ? 1 : 0),
      0
    );
}
