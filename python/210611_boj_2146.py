from collections import deque


def setIsland(y, x, setN):
    global N
    maps[y][x] = setN
    dq = deque()
    dq.append((y, x))

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]

            if 0 <= Y < N and 0 <= X < N:
                if maps[Y][X] == 1:
                    maps[Y][X] = setN
                    dq.append((Y, X))


def countBridgeLength(islandN):
    global N, res

    checkBridgeMaps = [[-1 for _ in range(N)] for _ in range(N)]
    dq = deque()

    for y in range(N):
        for x in range(N):
            if maps[y][x] == islandN:
                dq.append((y, x))
                checkBridgeMaps[y][x] = 0

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]

            if 0 <= Y < N and 0 <= X < N:
                if maps[Y][X] and maps[Y][X] != islandN and checkBridgeMaps[y][x]:
                    res = min(res, checkBridgeMaps[y][x])
                elif checkBridgeMaps[Y][X] == -1:
                    checkBridgeMaps[Y][X] = checkBridgeMaps[y][x] + 1
                    if checkBridgeMaps[Y][X] <= res:
                        dq.append((Y, X))


N = int(input())
maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
setN = 2
for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            setIsland(y, x, setN)
            setN += 1


res = 123456789

for i in range(2, setN):
    countBridgeLength(i)

print(res)
