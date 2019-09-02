import sys

sys.stdin = open('5648.txt')

T = int(input())

def halfMove(n):
    global atomList
    global result

    x = atomList[n][0]
    y = atomList[n][1]
    G = atomList[n][2]
    K = atomList[n][3]

    if G == 0:
        Y = y - 1
        if 0 <= x < 4000 and 0 <= Y < 4000:
            maps[y][x] = 0
            if maps[Y][x] == 0:
                maps[Y][x] = 1
                atomList[n] = [x, Y, G, K]
                return
            else:
                maps[Y][x] += 1
                atomList[n] = 0
                result += 1
                return
        else:
            maps[y][x] = 0
            atomList[n] = 0
            return
    elif G == 1:
        Y = y + 1
        if 0 <= x < 4000 and 0 <= Y < 4000:
            maps[y][x] = 0
            if maps[Y][x] == 0:
                maps[Y][x] = 1
                atomList[n] = [x, Y, G, K]
                result += 1
                return
            else:
                maps[Y][x] += 1
                atomList[n] = 0
                result += 1
                return
        else:
            maps[y][x] = 0
            atomList[n] = 0
            return
    elif G == 2:
        X = x - 1
        if 0 <= X < 4000 and 0 <= y < 4000:
            maps[y][x] = 0
            if maps[y][X] == 0:
                maps[y][X] = 1
                atomList[n] = [X, y, G, K]
                return
            else:
                maps[y][X] += 1
                atomList[n] = 0
                result += 1
                return
        else:
            maps[y][x] = 0
            atomList[n] = 0
            return
    elif G == 3:
        X = x + 1
        if 0 <= X < 4000 and 0 <= y < 4000:
            maps[y][x] = 0
            if maps[y][X] == 0:
                maps[y][X] = 1
                atomList[n] = [X, y, G, K]
                return
            else:
                maps[y][X] += 1
                atomList[n] = 0
                result += 1
                return
        else:
            maps[y][x] = 0
            atomList[n] = 0
            return


for case in range(1, T+1):
    N = int(input())
    maps = [[0 for x in range(4002)] for y in range(4002)]
    atomList = [0] * N
    for n in range(N):
        x, y, G, K = map(int, input().split())
        x = (2 * x) + 2000
        y = (2 * y) + 2000
        maps[y][x] = 1
        atomList[n] = [x, y, G, K]

    result = 0

    while atomList != [0] * N:
        for n in range(N):
            if atomList[n] != 0:
                halfMove(n)
            if atomList[n] != 0:
                halfMove(n)
    print(result)
