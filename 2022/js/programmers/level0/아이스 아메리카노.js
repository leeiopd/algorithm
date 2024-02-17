function solution(money) {
  var answer = [0, 0];
  let coffee = 5500;
  answer[1] = money % coffee;
  answer[0] = parseInt(money / coffee);
  return answer;
}
