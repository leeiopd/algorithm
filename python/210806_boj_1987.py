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

visited = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
           'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
           'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
           'Y': 0, 'Z': 0}

visited[maps[0][0]] = 1


def DFS(y, x, cnt):
    global res, R, C
    res = max(res, cnt)

    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]

        if 0 <= Y < R and 0 <= X < C and not visited[maps[Y][X]]:
            visited[maps[Y][X]] = 1
            DFS(Y, X, cnt+1)
            visited[maps[Y][X]] = 0


DFS(y, x, 1)
print(res)
