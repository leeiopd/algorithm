import sys
sys.stdin = open('13460.txt')


def check(maps):
    R = 0
    B = 0
    for y in range(1, N-1):
        if 'R' in maps[y]:
            R = 1
        if 'B' in maps[y]:
            B = 1
        if R*B:
            return False
    if not R and B:
        return True
    else:
        return False


def Rgame(maps):
    newM = [[0 for x in range(M)] for y in range(N)]
    for y in range(N):
        for x in range(M):
            newM[y][x] = maps[y][x]
    for y in range(N-2, 1, -1):
        for x in range(1, M-1):
            if newM[y][x] == 'R':
                X = x
                while True:
                    X += 1
                    if newM[y][X] != '.':
                        if newM[y][X] == 'O':
                            newM[y][x] = '.'
                            break
                        else:
                            newM[y][x] = '.'
                            newM[y][X-1] = 'R'
                            break

            if newM[y][x] == 'B':
                X = x
                while True:
                    X += 1
                    if newM[y][X] != '.':
                        if newM[y][X] == 'O':
                            return False
                        else:
                            newM[y][x] = '.'
                            newM[y][X-1] = 'B'
                            break
    if maps != newM and newM not in memory:
        return newM
    else:
        return False


def Lgame(maps):
    newM = [[0 for x in range(M)] for y in range(N)]
    for y in range(N):
        for x in range(M):
            newM[y][x] = maps[y][x]
    for y in range(1, N-1):
        for x in range(1, M-1):
            if newM[y][x] == 'R':
                X = x
                while True:
                    X -= 1
                    if newM[y][X] != '.':
                        if newM[y][X] == 'O':
                            newM[y][x] = '.'
                            break
                        else:
                            newM[y][x] = '.'
                            newM[y][X+1] = 'R'
                            break

            if newM[y][x] == 'B':
                X = x
                while True:
                    X -= 1
                    if newM[y][X] != '.':
                        if newM[y][X] == 'O':
                            return False
                        else:
                            newM[y][x] = '.'
                            newM[y][X+1] = 'B'
                            break
    if maps != newM and newM not in memory:
        return newM
    else:
        return False


def Ugame(maps):
    newM = [[0 for x in range(M)] for y in range(N)]
    for y in range(N):
        for x in range(M):
            newM[y][x] = maps[y][x]
    for y in range(1, N-1):
        for x in range(M-2, 1, -1):
            if newM[y][x] == 'R':
                Y = y
                while True:
                    Y -= 1
                    if newM[Y][x] != '.':
                        if newM[Y][x] == 'O':
                            newM[y][x] = '.'
                            break
                        else:
                            newM[y][x] = '.'
                            newM[Y+1][x] = 'R'
                            break

            if newM[y][x] == 'B':
                Y = y
                while True:
                    Y -= 1
                    if newM[Y][x] != '.':
                        if newM[Y][x] == 'O':
                            return False
                        else:
                            newM[y][x] = '.'
                            newM[Y+1][x] = 'B'
                            break
    if maps != newM and newM not in memory:
        return newM
    else:
        return False


def Dgame(maps):
    newM = [[0 for x in range(M)] for y in range(N)]
    for y in range(N):
        for x in range(M):
            newM[y][x] = maps[y][x]
    for y in range(1, N-1):
        for x in range(1, M-1):
            if newM[y][x] == 'R':
                Y = y
                while True:
                    Y += 1
                    if newM[Y][x] != '.':
                        if newM[Y][x] == 'O':
                            newM[y][x] = '.'
                            break
                        else:
                            newM[y][x] = '.'
                            newM[Y-1][x] = 'R'
                            break

            if newM[y][x] == 'B':
                Y = y
                while True:
                    Y -= 1
                    if newM[Y][x] != '.':
                        if newM[Y][x] == 'O':
                            return False
                        else:
                            newM[y][x] = '.'
                            newM[Y-1][x] = 'B'
                            break
    if maps != newM and newM not in memory:
        return newM
    else:
        return False


def Dfs(x, newM):
    global result
    if newM not in memory:
        memory.append(newM)

        print(memory)
    if x > result:
        return
    if check(newM):
        if x < result:
            result = x
            return
    Rtemp = Rgame(newM)
    if Rtemp:
        Dfs(x+1, Rtemp)

    Ltemp = Lgame(newM)
    if Ltemp:
        Dfs(x+1, Ltemp)

    Utemp = Ugame(newM)
    if Utemp:
        Dfs(x+1, Utemp)

    Dtemp = Dgame(newM)
    if Dtemp:
        Dfs(x+1, Dtemp)


N, M = map(int, input().split())

maps = []
memory = []
for n in range(N):
    maps.append(list(map(str, input())))
result = 999999
Dfs(0, maps)
print(result)
