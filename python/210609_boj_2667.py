import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
maps = []

for _ in range(N):
    maps.append(list(map(int, list(input().rstrip()))))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

blocks = []

for r in range(N):
    for c in range(N):
        if maps[r][c]:
            dq = deque()
            dq.append((r, c))
            maps[r][c] = 0
            cnt = 1
            while dq:
                y, x = dq.popleft()
                for i in range(4):
                    X = x + dx[i]
                    Y = y + dy[i]

                    if 0 <= Y < N and 0 <= X < N and maps[Y][X]:
                        maps[Y][X] = 0
                        cnt += 1
                        dq.append((Y, X))
            blocks.append(cnt)
print(len(blocks))
for b in sorted(blocks):
    print(b)
