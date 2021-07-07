import sys
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []

for _ in range(R):
    maps.append(list(map(int, input().split())))


def findMin(R, C):
    min = 123456789
    min_r = -1
    min_c = -1
    for r in range(R):
        for c in range(C):
            if (r+c) % 2 and maps[r][c] < min:
                min = maps[r][c]
                min_r = r
                min_c = c
    return min_r, min_c


def DFS(x, y, cnt, res, maps):
    global R, C
    if cnt == R * C - 1:
        print(res)
        return

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]

        if 0 <= Y < R and 0 <= X < C and maps[Y][X] != 0:
            tmp = maps[Y][X]
            maps[Y][X] = 0
            DFS(X, Y, cnt+1, res+move[i], maps)
            maps[Y][X] = tmp


if R % 2:
    for r in range(R):
        if r % 2:
            print("L"*(C-1), end="")
        else:
            print("R"*(C-1), end="")

        if r != R-1:
            print("D", end="")
        else:
            print("D")

elif C % 2:
    for c in range(C):
        if c % 2:
            print("U"*(R-1), end="")
        else:
            print("D"*(R-1), end="")

        if c != C-1:
            print("R", end="")
        else:
            print("R")

else:
    min_r, min_c = findMin(R, C)
    maps[min_r][min_c] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    move = {0: "R", 1: "D", 2: "L", 3: "U"}

    maps[0][0] = 0
    DFS(0, 0, 1, "", maps)
