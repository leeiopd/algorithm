from collections import deque

N, M = map(int, input().split())

maps = []

for _ in range(M):
    maps.append(list(map(int, input())))

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

queue = deque()
queue.append((0, 0, 0))

visited = [[(M*N)+1 for _ in range(N)] for _ in range(M)]

while queue:
    y, x, cnt = queue.popleft()

    if y == M-1 and x == N-1:
        print(cnt)
        break

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]

        if 0 <= Y < M and 0 <= X < N:
            if maps[Y][X] and cnt + 1 < visited[Y][X]:
                visited[Y][X] = cnt+1
                queue.append((Y, X, cnt + 1))
            elif not maps[Y][X] and cnt < visited[Y][X]:
                visited[Y][X] = cnt
                # queue.append((Y, X, cnt))
                queue.appendleft((Y, X, cnt))
