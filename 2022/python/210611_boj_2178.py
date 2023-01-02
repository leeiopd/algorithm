from collections import deque

N, M = map(int, input().split())

maps = []

for _ in range(N):
    maps.append(list(map(int, list(input()))))

dq = deque()
dq.append((0, 0))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while dq:
    y, x = dq.popleft()

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]

        if 0 <= Y < N and 0 <= X < M and maps[Y][X]:
            if maps[Y][X] == 1:
                maps[Y][X] = maps[y][x] + 1
                dq.append((Y, X))
            elif maps[Y][X] > maps[y][x] + 1:
                maps[Y][X] = maps[y][x] + 1
                dq.append((Y, X))

print(maps[N-1][M-1])
