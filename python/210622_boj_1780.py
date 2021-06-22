import sys
input = sys.stdin.readline

N = int(input())
maps = []
for _ in range(N):
    maps.append(input().split())

cntDic = {"-1": 0, "0": 0, "1": 0}


def DFS(y, x, n):
    if n == 1:
        cntDic[maps[y][x]] += 1
        return

    for i in range(y, y+n):
        for j in range(x, x+n):
            if maps[y][x] != maps[i][j]:
                DFS(y, x, n//3)
                DFS(y, x+n//3, n//3)
                DFS(y, x+(n//3*2), n//3)
                DFS(y+n//3, x, n//3)
                DFS(y+n//3, x+n//3, n//3)
                DFS(y+n//3, x+(n//3*2), n//3)
                DFS(y+(n//3*2), x, n//3)
                DFS(y+(n//3*2), x+n//3, n//3)
                DFS(y+(n//3*2), x+(n//3*2), n//3)
                return

    cntDic[maps[y][x]] += 1
    return


DFS(0, 0, N)


print(cntDic["-1"])
print(cntDic["0"])
print(cntDic["1"])
