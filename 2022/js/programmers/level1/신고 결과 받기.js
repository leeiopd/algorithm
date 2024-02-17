function solution(id_list, report, k) {
  const L = id_list.length;
  const answer = new Array(L).fill(0);

  const report2by2 = [];
  const stopList = [];
  for (let i = 0; i < L; i++) {
    report2by2[i] = new Array(L).fill(0);
  }

  for (r of report) {
    const tmp = r.split(" ");
    //             신고한사람                  신고당한사람
    report2by2[id_list.indexOf(tmp[0])][id_list.indexOf(tmp[1])]++;
  }

  for (let i = 0; i < L; i++) {
    let count = 0;
    for (let j = 0; j < L; j++) {
      count += report2by2[j][i] ? 1 : 0;
    }
    if (count >= k) {
      for (let z = 0; z < L; z++) {
        if (report2by2[z][i]) {
          answer[z]++;
        }
      }
    }
  }

  return answer;
}
