'''
아래 그림과 같은 미로가 있다. 100*100 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.

가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.

주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

아래의 예시에서는 도달 가능하다.




아래의 예시에서는 출발점이 (1, 1)이고, 도착점이 (11, 11)이며 도달이 불가능하다.



위의 예시는 공간상의 이유로 100x100이 아닌 16x16으로 주어졌음에 유의한다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

[출력]

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
'''
import sys
sys.stdin = open('1227.txt')

T = 10


def game(start_x, start_y):
    global flag
    route.append([start_x, start_y])

    while route:
        x, y = map(int, route.pop(-1))

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if check(X, Y):
                if maps[Y][X] == 0 or maps[Y][X] == 3:
                    if maps[Y][X] == 3:
                        flag = True
                        return
                    else:
                        maps[Y][X] = 9
                    route.append([X, Y])


def check(x, y):
    if x < 1:
        return False
    if x > 99:
        return False
    if y < 1:
        return False
    if y > 99:
        return False
    return True


def findStart():
    for y in range(size):
        for x in range(size):
            if maps[y][x] == 2:
                return x, y


for t in range(1, T+1):
    case = int(input())
    size = 100

    maps = [0] * size

    for i in range(size):
        maps[i] = list(map(int, input()))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, - 1]
    start_x,  start_y = findStart()
    route = []
    flag = False
    game(start_x, start_y)

    if flag:
        print('#{} 1'.format(case))
    else:
        print('#{} 0'.format(case))
