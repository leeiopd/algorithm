function solution(array, height) {
  const tallArray = array.filter((tall) => tall > height);
  return tallArray.length;
}
