import sys
from collections import deque
input = sys.stdin.readline


def BFS(s_y, s_x):
    global w, h

    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]

    dq = deque()
    dq.append((s_y, s_x))

    while dq:
        y, x = dq.popleft()

        for i in range(8):
            Y = y + dy[i]
            X = x + dx[i]
            if 0 <= Y < h and 0 <= X < w and maps[Y][X]:
                maps[Y][X] = 0
                dq.append((Y, X))


while True:
    w, h = map(int, input().split())
    if not w or not h:
        break
    maps = [0] * h

    for i in range(h):
        maps[i] = list(map(int, input().split()))
    res = 0
    for y in range(h):
        for x in range(w):
            if maps[y][x]:
                res += 1
                maps[y][x] = 0
                BFS(y, x)
    print(res)
