function solution(maps) {
  var answer = [];
  const x_max = maps[0].length;
  const y_max = maps.length;

  for (let y = 0; y < y_max; y++) {
    maps[y] = maps[y].split("").map((i) => {
      if (i === "X") return 0;
      return parseInt(i);
    });
  }

  for (let y = 0; y < y_max; y++) {
    for (let x = 0; x < x_max; x++) {
      if (!maps[y][x]) continue;
      let count = 0;
      const queue = [[y, x]];

      while (queue.length) {
        const [Y, X] = queue[0];
        queue.shift();

        if (!maps[Y][X]) continue;
        count += parseInt(maps[Y][X]);
        maps[Y][X] = 0;

        if (Y + 1 < y_max && maps[Y + 1][X]) queue.push([Y + 1, X]);
        if (Y - 1 >= 0 && maps[Y - 1][X]) queue.push([Y - 1, X]);
        if (X + 1 < x_max && maps[Y][X + 1]) queue.push([Y, X + 1]);
        if (X - 1 >= 0 && maps[Y][X - 1]) queue.push([Y, X - 1]);
      }

      answer.push(count);
    }
  }
  answer.sort((a, b) => (a > b ? 1 : -1));
  return answer.length ? answer : [-1];
}
