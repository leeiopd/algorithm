function solution(word) {
  var answer = 0;
  const alpha = ["A", "E", "I", "O", "U"];
  const dic = [];

  const makeDic = (memo) => {
    if (memo.length > 5) return;
    dic.push(memo);
    for (let i = 0; i < 5; i++) {
      if (dic.indexOf(memo + alpha[i]) === -1) {
        makeDic(memo + alpha[i]);
      }
    }
  };

  for (let i = 0; i < 5; i++) {
    makeDic(alpha[i]);
  }

  return dic.sort().indexOf(word) + 1;
}
