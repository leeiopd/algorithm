const REMOVE = ["a", "e", "i", "o", "u"];

function solution(my_string) {
  var answer = "";
  const tmp = my_string.split("").map((item) => {
    if (REMOVE.indexOf(item) === -1) answer += item;
  });
  return answer;
}
