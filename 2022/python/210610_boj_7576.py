from collections import deque


def printResult():
    global N, M

    res = 0
    for n in range(N):
        for m in range(M):
            if not maps[n][m]:
                return print(-1)
            res = max(res, maps[n][m])
    if res == -1:
        return print(0)
    return print(res-1)


M, N = map(int, input().split())
maps = [0] * N
for n in range(N):
    maps[n] = list(map(int, input().split()))

# 시작 위치 좌표 준비
dq = deque()
for n in range(N):
    for m in range(M):
        if maps[n][m] == 1:
            dq.append((n, m))

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

# BFS 로 시행
while dq:
    y, x = dq.popleft()

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]
        if 0 <= Y < N and 0 <= X < M and not maps[Y][X]:
            maps[Y][X] = maps[y][x] + 1
            dq.append((Y, X))

printResult()
