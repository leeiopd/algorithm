// i : 상자 번호
// order[i] : 택배 상차 순서
//

function solution(order) {
  const L = order.length;

  let orderIndex = 0;
  const stack = [];

  for (let i = 0; i <= L; i++) {
    if (i + 1 === order[orderIndex]) {
      orderIndex++;
      continue;
    }

    while (stack.length) {
      if (stack[stack.length - 1] === order[orderIndex]) {
        stack.pop();
        orderIndex++;
        continue;
      }
      break;
    }

    stack.push(i + 1);
  }

  return orderIndex;
}
