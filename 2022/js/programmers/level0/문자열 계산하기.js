function solution(my_string) {
  const array = my_string.split(" ");
  var answer = parseInt(array[0]);

  for (let i = 1; i < array.length; i++) {
    if (array[i] === "+") answer += parseInt(array[++i]);
    if (array[i] === "-") answer -= parseInt(array[++i]);
  }
  return answer;
}
