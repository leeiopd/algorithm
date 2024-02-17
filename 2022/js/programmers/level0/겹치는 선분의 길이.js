function solution(lines) {
  var answer = 0;

  const row = Array(201).fill(0);

  for (line of lines) {
    const start = line[0] + 100;
    const end = line[1] + 100;

    for (let i = start; i < end; i++) {
      row[i]++;
    }
  }

  row.forEach((i) => {
    if (i > 1) answer++;
  });

  return answer;
}
