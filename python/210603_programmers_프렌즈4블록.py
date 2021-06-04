def makeBoard(m, board):
    newBoard = []
    for i in range(m):
        newBoard.append(list(map(str, board[i])))
    return newBoard


def checkboard(m, n, board):
    deleteList = []
    for y in range(m-1):
        for x in range(n-1):
            if board[y][x] and board[y][x] == board[y][x+1] and board[y][x] == board[y+1][x] and board[y][x] == board[y+1][x+1]:
                deleteList.extend([[y, x], [y, x+1], [y+1, x], [y+1, x+1]])

    return deleteList


def deleteBlocks(board, deleteList):
    for d in deleteList:
        board[d[0]][d[1]] = 0
    return board


def setBoard(m, n, board):
    for y in range(m-1, -1, -1):
        for x in range(n):
            if board[y][x]:
                continue
            nextY = y
            while nextY > 0:
                nextY -= 1
                if board[nextY][x]:
                    board[nextY][x], board[y][x] = board[y][x], board[nextY][x]
                    break
    return board


def countBoard(m, n, board):
    cnt = 0
    for y in range(m):
        for x in range(n):
            if not board[y][x]:
                cnt += 1
    return cnt


def solution(m, n, board):
    board = makeBoard(m, board)

    while True:
        deleteList = checkboard(m, n, board)
        if not deleteList:
            break
        board = setBoard(m, n, deleteBlocks(board, deleteList))
    print(board)
    return print(countBoard(m, n, board))


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
