function solution(board) {
  var answer = 0;
  const L = board.length;

  const bombCheck = (y, x) => {
    if (x - 1 > -1 && !board[y][x - 1]) board[y][x - 1] = -1;
    if (x + 1 < L && !board[y][x + 1]) board[y][x + 1] = -1;
    if (y - 1 > -1 && !board[y - 1][x]) board[y - 1][x] = -1;
    if (y + 1 < L && !board[y + 1][x]) board[y + 1][x] = -1;
    if (x - 1 > -1 && y - 1 > -1 && !board[y - 1][x - 1])
      board[y - 1][x - 1] = -1;
    if (x + 1 < L && y + 1 < L && !board[y + 1][x + 1])
      board[y + 1][x + 1] = -1;
    if (x - 1 > -1 && y + 1 < L && !board[y + 1][x - 1])
      board[y + 1][x - 1] = -1;
    if (x + 1 < L && y - 1 > -1 && !board[y - 1][x + 1])
      board[y - 1][x + 1] = -1;
  };

  for (let i = 0; i < L; i++) {
    for (let j = 0; j < L; j++) {
      if (board[i][j] === 1) bombCheck(i, j);
    }
  }

  for (let i = 0; i < L; i++) {
    for (let j = 0; j < L; j++) {
      if (!board[i][j]) answer++;
    }
  }

  return answer;
}
