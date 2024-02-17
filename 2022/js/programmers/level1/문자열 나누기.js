function solution(s) {
  var answer = 0;

  let match = 0;
  let mismatch = 0;

  let index = 0;

  while (s.length || index < s.length) {
    if (s[0] === s[index]) match++;
    else mismatch++;

    if (match === mismatch) {
      s = s.slice(index + 1, s.length);
      answer++;
      index = 0;
      continue;
    }

    index++;
  }

  return answer;
}
