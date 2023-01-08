const NUMBERS = {
  zero: "0",
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

function solution(numbers) {
  let answer = "";
  let tmp = "";
  for (str of numbers) {
    tmp += str;
    if (NUMBERS[tmp]) {
      answer += NUMBERS[tmp];
      tmp = "";
    }
  }
  return parseInt(answer);
}
