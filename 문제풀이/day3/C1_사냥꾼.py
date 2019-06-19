'''
산속에서 사냥꾼이 토끼를 잡으려 한다.
사냥꾼 위치에서 8방향으로 총을 쏘는데 사냥꾼이나 바위뒤에 있는 토끼는 잡을 수 없다.
모든 사냥꾼이 있는 자리에서 토끼를 잡았을때 모두 몇마리를 잡을 수 있는지 잡은 토끼의 마리수를 출력한다.
입력값으로 1은 사냥군, 0은 바위, 2는 토끼를 의미한다.
아래의 그림처럼 사냥꾼이 2명이면 첫번째 사냥꾼(빨간색)인 경우 4마리를 잡을 수 있고 다른 사냥꾼(노란색)은 5마리를 잡아서 도합 9마리를 잡을 수 있다

N개가 주어지고 다음에 맵의 정보가 주어진다. (N은 최대 10)

잡을 수 있는 토끼의 마리수를 구한다.
'''

import sys

sys.stdin = open("C1_input.txt")

N = int(input())

maps = []

for y in range(N):
    maps.append(list(map(int, list(input()))))
cnt = 0

def hunt(x, y):
    global cnt
    x0 = x
    x1 = x
    y0 = y
    y1 = y
    while True:
        x0 -= 1
        if x < 0 or maps[y][x0] == 0 or maps[y][x0] == 1:
            break

        if maps[y][x0] == 2:
            maps[y][x0] = 9
            cnt += 1

    while True:
        x1 += 1
        if x1 > N-1 or maps[y][x1] == 0 or maps[y][x1] == 1:
            break

        if maps[y][x1] == 2:
            maps[y][x1] = 9
            cnt += 1

    while True:
        y0 -= 1
        if y0 < 0 or maps[y0][x] == 0 or maps[y0][x] == 1:
            break

        if maps[y0][x] == 2:
            maps[y0][x] = 9
            cnt += 1

    while True:
        y1 += 1
        if y1 > N-1 or maps[y1][x] == 0 or maps[y1][x] == 1:
            break

        if maps[y1][x] == 2:
            maps[y1][x] = 9
            cnt += 1

    x0 = x
    y0 = y
    while True:
        x0 -= 1
        if x < 0:
            break
        y0 -= 1
        if y < 0:
            break

        if maps[y0][x0] == 0 or maps[y0][x0] == 1:
            break

        if maps[y0][x0] == 2:
            maps[y0][x0] = 9
            cnt += 1

    x1 = x
    y1 = y
    while True:
        x1 += 1
        if x1 > N-1:
            break

        y1 += 1
        if y1 > N - 1:
            break
        if  maps[y1][x1] == 0 or maps[y1][x1] == 1:
            break

        if maps[y1][x1] == 2:
            maps[y1][x1] = 9
            cnt += 1

    x0 = x
    y1 = y
    while True:
        x0 -= 1
        if x < 0:
            break
        y1 += 1
        if y1 > N - 1:
            break
        if  maps[y1][x0] == 0 or maps[y1][x0] == 1:
            break

        if maps[y1][x0] == 2:
            maps[y1][x0] = 9
            cnt += 1

    x1 = x
    y0 = y
    while True:
        x1 += 1
        if x1 > N - 1:
            break
        y0 -= 1
        if y < 0 :
            break

        if maps[y0][x1] == 0 or maps[y0][x1] == 1:
            break

        if maps[y0][x1] == 2:
            maps[y0][x1] = 9
            cnt += 1





for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            hunt(x, y)

print(cnt)