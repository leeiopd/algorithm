const BABBLINGS = ["aya", "ye", "woo", "ma"];

function solution(babbling) {
  var answer = 0;

  babbling = babbling.map((item) => {
    for (let i = 0; i < 4; i++) {
      while (true) {
        const newItem = item.replace(BABBLINGS[i], i.toString());
        if (item === newItem) break;
        item = newItem;
      }
    }
    return item;
  });

  for (let i = 0; i < babbling.length; i++) {
    if (isNaN(babbling[i])) continue;

    let flag = 1;
    for (let j = 1; j < babbling[i].length; j++) {
      if (babbling[i][j] === babbling[i][j - 1]) {
        flag = 0;
        break;
      }
    }
    if (flag) answer++;
  }

  return answer;
}
