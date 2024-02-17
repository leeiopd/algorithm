function solution(k, tangerine) {
  var answer = 0;

  const tangerineCount = {};

  for (i of tangerine) {
    if (tangerineCount?.[i]) {
      tangerineCount[i]++;
      continue;
    }
    tangerineCount[i] = 1;
  }

  const typeCount = new Array(10000000).fill(0);

  for (i in tangerineCount) {
    typeCount[tangerineCount[i]]++;
  }

  let totalCount = 0;

  for (let i = 10000000; i > 0; i--) {
    if (typeCount[i]) {
      for (let j = 1; j <= typeCount[i]; j++) {
        answer++;
        totalCount += i;
        if (totalCount >= k) return answer;
      }
    }
  }

  return answer;
}
