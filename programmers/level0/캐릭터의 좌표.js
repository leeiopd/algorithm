function solution(keyinput, board) {
  let position = [0, 0];
  const MAX_X = (board[0] - 1) / 2;
  const MIN_X = ((board[0] - 1) / 2) * -1;
  const MAX_Y = (board[1] - 1) / 2;
  const MIN_Y = ((board[1] - 1) / 2) * -1;

  for (key of keyinput) {
    switch (key) {
      case "up":
        position[1] += position[1] + 1 <= MAX_Y ? 1 : 0;
        break;
      case "down":
        position[1] -= position[1] - 1 >= MIN_Y ? 1 : 0;
        break;
      case "right":
        position[0] += position[0] + 1 <= MAX_X ? 1 : 0;
        break;
      case "left":
        position[0] -= position[0] - 1 >= MIN_X ? 1 : 0;
        break;
    }
  }

  return position;
}
