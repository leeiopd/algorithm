import sys

sys.stdin = open("장기.txt")

N, M = map(int, input().split())

maps = [[0 for x in range(M+1)] for y in range(N+1)]

Y, X, y_, x_ = map(int, input().split())
cnt = 0
queue = [[X, Y, cnt]]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
while queue:
    x, y, cnt = queue.pop(0)


    for i in range(8):
        X = x + dx[i]
        Y = y + dy[i]

        if Y >= 1 and Y < N and X >= 1 and X < M and maps[Y][X] == 0:
            if Y == y_ and X == x_:
                result = cnt
                break
            maps[Y][X] = cnt
            queue.append([X, Y, cnt+1])

print(result-1)