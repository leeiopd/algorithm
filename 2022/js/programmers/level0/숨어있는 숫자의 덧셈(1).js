function solution(my_string) {
  return my_string
    .split("")
    .reduce((acc, cur, idx) => (acc += isNaN(cur) ? 0 : parseInt(cur)), 0);
}
