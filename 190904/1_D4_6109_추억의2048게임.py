'''
2048이라는 추억의 게임을 아는가? 2048은 한 때 유명했던 1인용 게임으로, 격자 위에서 숫자가 적힌

타일들을 밀어서 합치고 최종적으로 2048을 만들어 내는 것이 목표인 게임이다.

한번 타일을 밀 때는 상하좌우를 정해서 밀어야 한다.

방향을 정하면 격자 위에 있는 모든 타일이 그 방향으로 밀린다.

만약 어떤 타일이 밀리는 방향에 다른 타일이 있고, 두 타일에 적힌 숫자가 같다면 두 타일은 합쳐져

새로운 하나의 타일이 되고 이 타일에 적힌 숫자는 합쳐진 숫자들의 합이 된다.

이렇게 합쳐져서 만들어진 새로운 타일은 숫자가 같은 다른 타일이 밀려와도 합쳐져서는 안 된다.

만약 같은 숫자가 적힌 타일이 세 개 이상 있을 때는 헷갈리는 경우를 없애기 위해 빨리 벽에 닿게 될 타일을 먼저 민다고

생각한다.

예를 들어 “2 2 4 2 2 2”가 적힌 타일들이 있을 때, 이 타일들을 왼쪽으로 밀면 결과는 “4 4 4 2 0 0”이 된다.

0은 타일이 없는 빈 칸을 나타낸다.

위의 그림은 4×4 크기의 격자(일반적인 2048 게임)에서 모든 타일을 오른쪽으로 이동시킨 예이다.

우리는 2048게임을 N×N 크기의 격자에서 하려고 한다.

현재 격자에 어떤 식으로 타일이 있는지 주어지고, 타일들을 이동시킬 방향이 주어질 때,

타일을 모두 이동시키고 나면 격자가 어떻게 변할 지 계산하는 프로그램을 작성하라.



[입력]

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤20)과 하나의 문자열 S가 공백 하나로 구분되어 주어진다.

S는 “left”, “right”, “up”, “down”의 넷 중 하나이며 각각 타일들을 왼쪽, 오른쪽, 위쪽, 아래쪽으로 이동시키겠다는 뜻이다.

다음 N개의 줄의 i번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다.

이 정수들은 0이거나 2이상 1024이하의 2의 제곱수들이다.

i번째 줄의 j번째 정수는 격자의 위에서 i번째 줄의 왼쪽에서 j번째에 있는 칸에 있는 타일에 어떤 정수가 적혀 있는지 나타내며,

0이면 이 칸에 타일이 없음을 의미한다.


[출력]

각 테스트 케이스마다 ‘#t’(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 줄을 띄운 후,

N줄에 걸쳐 격자의 어떤 위치에 어떤 숫자가 적힌 타일이 있는지 입력 형식과 같은 형식으로 출력한다.
'''
import sys
sys.stdin = open('6109.txt')

T = int(input())


def upMove(x, y):
    global maps
    while True:
        if maps[y][x] != 0:
            Y = y - 1
            if 0 <= Y < N:
                if maps[Y][x] != 0:
                    if maps[Y][x] == maps[y][x]:
                        maps[Y][x] = maps[y][x] * 2
                        maps[y][x] = -1
                        return
                    elif maps[Y][x] == -1:
                        maps[Y][x] = maps[y][x]
                        maps[y][x] = 0
                        return
                    return
                else:
                    maps[Y][x] = maps[y][x]
                    maps[y][x] = 0
            else:
                return
        y -= 1
        if y < 0 or y >= N or x < 0 or x >= N:
            return


def downMove(x, y):
    global maps
    while True:
        if maps[y][x] != 0:
            Y = y + 1
            if 0 <= Y < N:
                if maps[Y][x] != 0:
                    if maps[Y][x] == maps[y][x]:
                        maps[Y][x] = maps[y][x] * 2
                        maps[y][x] = -1
                        return
                    elif maps[Y][x] == -1:
                        maps[Y][x] = maps[y][x]
                        maps[y][x] = 0
                        return
                    return
                else:
                    maps[Y][x] = maps[y][x]
                    maps[y][x] = 0
            else:
                return
        y += 1
        if y < 0 or y >= N or x < 0 or x >= N:
            return


def rightMove(x, y):
    global maps
    while True:
        if maps[y][x] != 0:
            X = x + 1
            if 0 <= X < N:
                if maps[y][X] != 0:
                    if maps[y][X] == maps[y][x]:
                        maps[y][X] = maps[y][x] * 2
                        maps[y][x] = 0
                        maps[y][X-1] = -1
                        return
                    elif maps[y][X] == -1:
                        maps[y][X] = maps[y][x]
                        maps[y][x] = 0
                        return
                    return
                else:
                    maps[y][X] = maps[y][x]
                    maps[y][x] = 0
            else:
                return
        x += 1
        if y < 0 or y >= N or x < 0 or x >= N:
            return


def leftMove(x, y):
    global maps
    while True:
        if maps[y][x] != 0:
            X = x - 1
            if 0 <= X < N:
                if maps[y][X] != 0:
                    if maps[y][X] == maps[y][x]:
                        maps[y][X] = maps[y][x] * 2
                        maps[y][x] = 0
                        maps[y][X+1] = -1
                        return
                    elif maps[y][X] == -1:
                        maps[y][X] = maps[y][x]
                        maps[y][x] = 0
                        return
                    return
                else:
                    maps[y][X] = maps[y][x]
                    maps[y][x] = 0
            else:
                return
        x -= 1
        if y < 0 or y >= N or x < 0 or x >= N:
            return


def game(x, y, S):
    if S == 'up':
        upMove(x, y)
    elif S == 'down':
        downMove(x, y)
    elif S == 'right':
        rightMove(x, y)
    else:
        leftMove(x, y)


for case in range(1, T+1):
    N, S = map(str, input().split())
    N = int(N)
    maps = []

    for n in range(N):
        maps.append(list(map(int, input().split())))

    if S == 'up':
        for y in range(1, N):
            for x in range(N):
                game(x, y, S)
    elif S == 'down':
        for y in range(N-2, -1, -1):
            for x in range(N):
                game(x, y, S)
    elif S == 'right':
        for x in range(N-1, -1, -1):
            for y in range(N):
                game(x, y, S)
    else:
        for x in range(1, N):
            for y in range(N):
                game(x, y, S)

    for y in range(N):
        for x in range(N):
            if maps[y][x] == -1:
                maps[y][x] = 0

    print('#{}'.format(case))
    for n in range(N):
        print(' '.join(map(str, maps[n])))
