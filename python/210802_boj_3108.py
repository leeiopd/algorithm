from collections import deque

N = int(input())

maps = [[0 for _ in range(2001)] for _ in range(2001)]
startingQue = deque()

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(x1, x2+1):
        maps[y1][i] = 1
        maps[y2][i] = 1

    for i in range(y1, y2+1):
        maps[i][x1] = 1
        maps[i][x2] = 1
    startingQue.append((y1, x1))

startingQue.append((1000, 1000))


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
visited = [[0 for _ in range(2001)] for _ in range(2001)]
res = 0

for q in startingQue:
    if visited[q[0]][q[1]]:
        continue

    res += 1
    queue = deque()
    queue.append(q)
    while queue:
        qY, qX = queue.popleft()

        if visited[qY][qX]:
            continue

        visited[qY][qX] = 1

        for i in range(4):
            Y = qY + dy[i]
            X = qX + dx[i]

            if 0 <= Y <= 2000 and 0 <= X <= 2000:
                if maps[Y][X] and not visited[Y][X]:
                    queue.append((Y, X))

print(res-1)
