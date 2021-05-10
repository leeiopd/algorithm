import sys

sys.stdin = open("09_input.txt")


T = 10
# 1은 N극 성질을 가지는 자성체를 2는 S극
# 1 down
# 2 up

def magnetic(x, y, n):
    if y < 99 and n == 1:
        if maps[y+1][x] == 2:
            return

        elif maps[y+1][x] == 0:
            maps[y][x] = 0
            maps[y+1][x] = 1
            return

    elif y > 0 and n == 2:
        if maps[y-1][x] == 1:
            return

        elif maps[y-1][x] == 0:
            maps[y][x] = 0
            maps[y-1][x] = 2
            return

def check(x, y):
    global result
    if y < 99:
        if maps[y+1][x] == 2:
            result += 1

    elif y < 98:
        if maps[y+1][x] == 1 and maps[y+2][x] == 2:
            result += 1

    elif y < 98:
        if maps[y - 1][x] == 2 and maps[y + 2][x] == 2:
            result += 1



for case in range(1, T+1):
    N = int(input())
    maps = []
    for n in range(N):
        long = list(map(int, input().split()))
        maps.append(long)

    for y in range(N):
        for x in range(N):
            mag = maps[y][x]
            magnetic(x, y, mag)

    result = 0
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 1:
                check(x, y)
    print(f'#{case} {result}')

