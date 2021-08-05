maps = []

for _ in range(9):
    maps.append(list(map(int, input().split())))

zeroPosition = []
for y in range(9):
    for x in range(9):
        if not maps[y][x]:
            zeroPosition.append([y, x])

resFlag = False


def getNums(y, x):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if maps[i][x] in nums:
            nums.remove(maps[i][x])
        if maps[y][i] in nums:
            nums.remove(maps[y][i])

    if not nums:
        return nums

    I = y//3
    J = x//3

    for i in range(I*3, (I+1) * 3):
        for j in range(J*3, (J+1) * 3):
            if not nums:
                return nums
            if maps[i][j] in nums:
                nums.remove(maps[i][j])
    return nums


def DFS(cnt):
    global resFlag
    if resFlag:
        return

    if cnt == len(zeroPosition):
        resFlag = True
        for y in range(9):
            print(" ".join(map(str, maps[y])))
        return

    Y, X = zeroPosition[cnt]

    numList = getNums(Y, X)

    for n in numList:
        maps[Y][X] = n
        DFS(cnt+1)
    maps[Y][X] = 0


DFS(0)
