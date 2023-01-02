import sys
input = sys.stdin.readline


def DFS(y, x, n):
    if n == 1:
        print(maps[y][x], end="")
        return

    for i in range(y, y+n):
        for j in range(x, x+n):
            if maps[y][x] != maps[i][j]:
                print("(", end="")
                DFS(y, x, n//2)
                DFS(y, x+n//2, n//2)
                DFS(y+n//2, x, n//2)
                DFS(y+n//2, x+n//2, n//2)
                print(")", end="")
                return

    print(maps[y][x], end="")
    return


N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, list(input().rstrip()))))

DFS(0, 0, N)
