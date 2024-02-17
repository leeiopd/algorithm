function solution(babbling) {
  var answer = 0;

  const babCehck = (bab) => {
    if (bab.length === 1 && bab[0].length) {
      answer++;
      return true;
    }
  };

  for (bab of babbling) {
    let tmp = "";

    while (true) {
      const L = tmp.length;
      if (L > tmp) break;

      if (bab.slice(L, L + 2) === "ye") {
        tmp += "ye";
        continue;
      }
      if (bab.slice(L, L + 2) === "ma") {
        tmp += "ma";
        continue;
      }
      if (bab.slice(L, L + 3) === "aya") {
        tmp += "aya";
        continue;
      }
      if (bab.slice(L, L + 3) === "woo") {
        tmp += "woo";
        continue;
      }

      if (tmp.length === L) break;
    }

    if (tmp === bab) answer++;
  }
  return answer;
}
