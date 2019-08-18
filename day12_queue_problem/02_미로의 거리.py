'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.

이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.

경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100

0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys

sys.stdin = open("02_input.txt")

T = int(input())


def start(maps):
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 2:
                return x, y


def check(x, y, i):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    X = x + dx[i]
    Y = y + dy[i]

    if i == 0:
        if X < N:
            if maps[Y][X] == 0 or maps[Y][X] == 3:
                return X, Y
    elif i == 1:
        if X > -1:
            if maps[Y][X] == 0 or maps[Y][X] == 3:
                return X, Y
    elif i == 2:
        if Y < N:
            if maps[Y][X] == 0 or maps[Y][X] == 3:
                return X, Y
    elif i == 3:
        if Y > -1:
            if maps[Y][X] == 0 or maps[Y][X] == 3:
                return X, Y
    return False


def go(maps, x, y):
    global cnt, flag
    if maps[y][x] == 3:
        cnt -= 1
        flag = 1
        return

    maps[y][x] = 9
    for i in range(4):
        if check(x, y, i):
            X, Y = check(x, y, i)
            cnt += 1
            go(maps, X, Y)
        if flag == 1:
            return
    cnt -= 1


for case in range(1, T+1):
    N = int(input())

    maps = []
    for n in range(N):
        maps.append(list(map(int, input())))

    x, y = start(maps)
    i = 0
    cnt = 0
    flag = 0

    go(maps, x, y)
    if flag == 0:
        cnt = 0
    print(f'#{case} {cnt}')
