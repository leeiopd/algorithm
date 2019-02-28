import sys

sys.stdin = open("10_input.txt")

T = int(input())


def check(maps):
    for start_y in range(N):
        for start_x in range(N):
            if maps[start_y][start_x] != 0:
                dx = 0
                dy = 0
                X = 0
                Y = 0
                while True:
                    if maps[start_y][start_x + dx] != 0:
                        dx += 1
                    else:
                        X = dx
                    if maps[start_y + dy][start_x] != 0:
                        dy += 1
                    else:
                        Y = dy
                    if X != 0 and Y != 0:
                        break

                result.append([X * Y, Y, X])
                for dy in range(Y):
                    for dx in range(X):
                        maps[start_y + dy][start_x + dx] = 0


for case in range(1, T + 1):
    N = int(input())

    maps = []

    for n in range(N):
        maps.append(list(map(int, input().split())))

    result = []

    check(maps)

    result.sort()
    result.sort()

    print(f'#{case} {len(result)}', end=' ')
    for i in result:
        print(f'{i[1]} {i[2]}', end=' ')
    print()