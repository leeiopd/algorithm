function solution(want, number, discount) {
  var answer = 0;

  for (let i = 0; i <= discount.length - 10; i++) {
    const check = new Array(number.length).fill(0);
    for (let j = i; j < i + 10; j++) {
      if (want.indexOf(discount[j]) === -1) {
        break;
      }

      check[want.indexOf(discount[j])]++;
    }

    if (check.toString() === number.toString()) {
      answer++;
    }
  }

  return answer;
}
