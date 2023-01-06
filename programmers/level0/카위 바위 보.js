const WINS = { 0: 5, 2: 0, 5: 2 };

function solution(rsp) {
  return rsp
    .split("")
    .map((item) => WINS[item])
    .join("");
}
