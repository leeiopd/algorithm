'''
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.

보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).

4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.



그리고 흑, 백이 번갈아가며 돌을 놓는다.

처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.



플레이어는 빈공간에 돌을 놓을 수 있다.

단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.

(여기에서 "사이"란 가로/세로/대각선을 의미한다.)

(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.



이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.

만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.

보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.


 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.

그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.

돌의 색이 1이면 흑돌, 2이면 백돌이다.

만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.

돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

 [출력]

각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.

흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.
'''
import sys
sys.stdin = open('4615.txt')

T = int(input())


def setting():
    if N == 5:
        maps[2][2] = 2
        maps[2][3] = 1
        maps[3][2] = 1
        maps[3][3] = 2
    elif N == 7:
        maps[3][3] = 2
        maps[3][4] = 1
        maps[4][3] = 1
        maps[4][4] = 2
    else:
        maps[4][4] = 2
        maps[4][5] = 1
        maps[5][4] = 1
        maps[5][5] = 2


def checkR(x, y, D):
    Xr = x
    if x < N-1:
        for i in range(N-1, x, -1):
            if maps[y][i] == D:
                Xr = i
            elif maps[y][i] == 0:
                Xr = x
    return Xr-x


def checkL(x, y, D):
    Xl = x
    if x > 0:
        for i in range(1, x):
            if maps[y][i] == D:
                Xl = i
            elif maps[y][i] == 0:
                Xl = x
    return x - Xl


def checkU(x, y, D):
    Yu = y
    if y > 0:
        for i in range(1, y):
            if maps[i][x] == D:
                Yu = i
            elif maps[i][x] == 0:
                Yu = y
    return y - Yu


def checkD(x, y, D):
    Yd = y
    if y < N-1:
        for i in range(N-1, y, -1):
            if maps[i][x] == D:
                Yd = i
            elif maps[i][x] == 0:
                Yd = y
    return Yd - y


def checkRU(x, y, D):
    cnt = 0
    X = x
    Y = y
    while True:
        if X + 1 < N and Y - 1 > 0:
            X += 1
            Y -= 1
            cnt += 1
        else:
            break

    X = x
    Y = y
    check = 0
    for i in range(1, cnt+1):
        X += 1
        Y -= 1
        if maps[Y][X] == 0:
            check = 0
        elif maps[Y][X] == D:
            check = i
    return check


def checkLU(x, y, D):
    cnt = 0
    X = x
    Y = y
    while True:
        if X - 1 > 0 and Y - 1 > 0:
            X -= 1
            Y -= 1
            cnt += 1
        else:
            break

    X = x
    Y = y
    check = 0
    for i in range(1, cnt+1):
        X -= 1
        Y -= 1

        if maps[Y][X] == 0:
            check = 0
        elif maps[Y][X] == D:
            check = i
    return check


def checkRD(x, y, D):
    cnt = 0
    X = x
    Y = y
    while True:
        if X + 1 < N and Y + 1 < N:
            X += 1
            Y += 1
            cnt += 1
        else:
            break
    X = x
    Y = y
    check = 0
    for i in range(1, cnt+1):
        X += 1
        Y += 1
        if maps[Y][X] == 0:
            check = 0
        elif maps[Y][X] == D:
            check = i
    return check


def checkLD(x, y, D):
    cnt = 0
    X = x
    Y = y
    while True:
        if X - 1 > 0 and Y + 1 < N:
            X -= 1
            Y += 1
            cnt += 1
        else:
            break
    X = x
    Y = y
    check = 0
    for i in range(1, cnt+1):
        X -= 1
        Y += 1
        if maps[Y][X] == 0:
            check = 0
        elif maps[Y][X] == D:
            check = i
    return check


def checkMap(x, y, D):
    Ucnt = checkU(x, y, D)
    Dcnt = checkD(x, y, D)
    Rcnt = checkR(x, y, D)
    Lcnt = checkL(x, y, D)
    RUcnt = checkRU(x, y, D)
    LUcnt = checkLU(x, y, D)
    RDcnt = checkRD(x, y, D)
    LDcnt = checkLD(x, y, D)

    for u in range(1, Ucnt):
        X = x
        Y = y - u
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)
    for d in range(1, Dcnt):
        X = x
        Y = y + d
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)
    for r in range(1, Rcnt):
        X = x + r
        Y = y
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)
    for l in range(1, Lcnt):
        X = x - l
        Y = y
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)

    for ru in range(1, RUcnt):
        X = x + ru
        Y = y - ru
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)

    for lu in range(1, LUcnt):
        X = x - lu
        Y = y - lu
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)

    for rd in range(1, RDcnt):
        X = x + rd
        Y = y + rd
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)

    for ld in range(1, LDcnt):
        X = x - ld
        Y = y + ld
        if maps[Y][X] != D:
            maps[Y][X] = D
            checkMap(X, Y, D)


def count():
    black = 0
    white = 0

    for y in range(1, N):
        for x in range(1, N):
            if maps[y][x] == 1:
                black += 1
            if maps[y][x] == 2:
                white += 1
    return black, white


for case in range(1, T+1):
    N, M = map(int, input().split())
    N += 1
    maps = []
    for n in range(N):
        maps.append([0] * N)

    setting()

    turns = []
    for m in range(M):
        turns.append(list(map(int, input().split())))

    for turn in turns:
        x = turn[0]
        y = turn[1]
        D = turn[2]
        maps[y][x] = D
        checkMap(x, y, D)

    black, white = count()
    print('#{} {} {}'.format(case, black, white))
