function solution(queue1, queue2) {
  const L = queue1.length;
  let value = queue1.reduce((start, add, idx) => start + add - queue2[idx], 0);

  const queue = [...queue1, ...queue2];

  let p1 = queue1.length - 1;
  let p2 = queue.length - 1;
  let cnt = 0;

  for (let i = 0; i < L * 4; i++) {
    if (!value) break;
    cnt++;
    if (value < 0) {
      p1 = (p1 + 1) % queue.length;
      value += queue[p1] * 2;
    } else {
      p2 = (p2 + 1) % queue.length;
      value -= queue[p2] * 2;
    }
  }

  return value ? -1 : cnt;
}
solution([3, 2, 7, 2], [4, 6, 5, 1]);
