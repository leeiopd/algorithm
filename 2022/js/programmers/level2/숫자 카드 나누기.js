function solution(arrayA, arrayB) {
  arrayA.sort((a, b) => (a > b ? 1 : -1));
  arrayB.sort((a, b) => (a > b ? 1 : -1));

  const getResult = (arrayA, arrayB) => {
    const diffList = [];

    for (let i = arrayA[0]; i > 1; i--) {
      let flag = true;
      for (a of arrayA) {
        if (a % i) {
          flag = false;
          break;
        }
      }
      if (flag) diffList.push(i);
    }

    if (!diffList.length) return 0;

    for (d of diffList) {
      let flag = true;
      for (b of arrayB) {
        if (b % d === 0) {
          flag = false;
          break;
        }
      }
      if (flag) return d;
    }
    return 0;
  };

  const result = [getResult(arrayA, arrayB), getResult(arrayB, arrayA)];
  result.sort((a, b) => (a > b ? 1 : -1));
  return result[result.length - 1];
}
