def getDouble(n):
    return int(n) * 2


def solution(rectangle, characterX, characterY, itemX, itemY):
    # charcterX, charcterY는 1 이상 50 이하인 자연수
    maps = [[0 for _ in range(102)] for _ in range(102)]

    for rect in rectangle:
        x1, y1, x2, y2 = map(getDouble, rect)
        for j in range(y1, y2+1):
            for i in range(x1, x2+1):
                maps[j][i] = 1

    for rect in rectangle:
        x1, y1, x2, y2 = map(getDouble, rect)
        for j in range(y1+1, y2):
            for i in range(x1+1, x2):
                maps[j][i] = 0

    cnt = 0
    for j in range(102):
        cnt += sum(maps[j])

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    direction = 0

    characterY, characterX, itemY, itemX = map(
        getDouble, [characterY, characterX, itemY, itemX])

    res = 0
    while True:
        maps[characterY][characterX] = 0

        if characterY == itemY and characterX == itemX:
            break

        while True:
            if maps[characterY+dy[direction]][characterX+dx[direction]]:
                break
            direction = (direction + 1) % 4

        characterY += dy[direction]
        characterX += dx[direction]
        res += 1

    return min((cnt-res)//2, res//2)


print(solution([[2, 1, 3, 9], [1, 6, 10, 8], [
      7, 2, 9, 10], [4, 3, 11, 4]], 2, 2, 9, 5))
