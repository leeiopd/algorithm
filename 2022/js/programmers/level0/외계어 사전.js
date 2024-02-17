function solution(spell, dic) {
  var answer = 2;
  const newSpell = spell.sort().join("");
  dic
    .map((item) => item.split("").sort().join(""))
    .forEach((item) => {
      if (item === newSpell) answer = 1;
    });

  return answer;
}
