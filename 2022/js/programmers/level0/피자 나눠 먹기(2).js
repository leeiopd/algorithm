const PIZZA = 6;

function solution(n) {
  for (let i = 1; i <= 50; i++) {
    if ((6 * i) % n === 0) return i;
  }
}
