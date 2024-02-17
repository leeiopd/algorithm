function solution(ingredient) {
  var answer = 0;
  const stack = [];
  for (i of ingredient) {
    stack.push(i);

    if (stack.length >= 4) {
      if (stack.slice(stack.length - 4, stack.length).join("") === "1231") {
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        answer++;
      }
    }
  }
  return answer;
}
