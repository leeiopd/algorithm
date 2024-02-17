const GENERAL = 5;
const SOLIDER = 3;

function solution(hp) {
  var answer = 0;

  answer += parseInt(hp / GENERAL);
  hp = hp % GENERAL;
  answer += parseInt(hp / SOLIDER);
  hp = hp % SOLIDER;
  answer += hp;
  return answer;
}
