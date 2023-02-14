function solution(numbers) {
  const L = numbers.length;
  var answer = new Array(L).fill(-1);

  const stack = [];

  for (let i = 0; i < L; i++) {
    while (stack.length) {
      // stack 마지막 수 (직전 index 숫자) 보다, 작을경우 break;
      // 감소하거나 같을 경우
      if (numbers[stack[stack.length - 1]] >= numbers[i]) break;

      // 증가 했을 경우
      answer[stack.pop()] = numbers[i];
    }

    stack.push(i);
  }
  return answer;
}
