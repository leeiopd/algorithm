function solution(cards) {
  var answer = 0;

  for (let i = 0; i < cards.length; i++) {
    const visited = new Array(cards.length).fill(1);
    let first_result = 0;
    const dfs = (index, count) => {
      if (count === cards.length) return;

      if (!visited[index - 1]) {
        return (first_result = count);
      }

      visited[index - 1] = 0;
      dfs(cards[index - 1], count + 1);
    };

    dfs(cards[i], 0);

    if (!first_result) continue;

    let second_result;
    for (let j = 0; j < cards.length; j++) {
      if (!visited[j]) continue;
      const dfs = (index, count) => {
        if (count === cards.length) return;

        if (!visited[index - 1]) {
          return (second_result = count);
        }

        visited[index - 1] = 0;
        dfs(cards[index - 1], count + 1);
      };

      dfs(cards[j], 0);
      answer =
        answer < first_result * second_result
          ? first_result * second_result
          : answer;
    }
  }
  return answer;
}
