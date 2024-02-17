function solution(A, B) {
  let tmp = A.split("");
  for (let i = 0; i <= A.length; i++) {
    if (tmp.join("") === B) return i;
    tmp.unshift(tmp[A.length - 1]);
    tmp.pop();
  }
  return -1;
}
