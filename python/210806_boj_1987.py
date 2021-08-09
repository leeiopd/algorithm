import sys
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []

for _ in range(R):
    maps.append(list(input().rstrip()))

x = y = 0

res = 0

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

visited = [0] * 26
visited[ord(maps[0][0]) - 65] = 1


def DFS(y, x, cnt):
    global res, R, C
    res = max(res, cnt)

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]

        if 0 <= Y < R and 0 <= X < C and not visited[ord(maps[Y][X]) - 65]:
            visited[ord(maps[Y][X]) - 65] = 1
            DFS(Y, X, cnt+1)
            visited[ord(maps[Y][X]) - 65] = 0


DFS(y, x, 1)
print(res)
