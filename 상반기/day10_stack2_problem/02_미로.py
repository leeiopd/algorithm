import sys

sys.stdin = open("02_input.txt")

T = int(input())

def start(maps):
    for y in range(N):
        for x in range(N):
            if maps[y][x] == '2':
                return x, y


def check(X, Y):
    if X < 0 or X >= N: return False
    if Y < 0 or Y >= N: return False
    if maps[Y][X] == '1':
        return False
    if maps[Y][X] == '9':
        return False
    return True



def go(x, y):
    global flag, maps
    if maps[y][x] == '3':
        flag = True
        return

    maps[y][x] = '9'


    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]

        if check(X, Y):

            go(X, Y)


for case in range(1, T+1):
    N = int(input())
    maps = []
    flag = False
    visited = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    for n in range(N):
        maps.append(list(input()))
    start_x, start_y = start(maps) # 시작점 찾기


    go(start_x, start_y)


    if flag == True:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')