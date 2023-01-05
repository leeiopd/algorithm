function solution(my_string) {
  return my_string
    .split("")
    .filter((item) => !isNaN(item))
    .sort((a, b) => a - b)
    .map((item) => parseInt(item));
}
