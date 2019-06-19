import sys

sys.stdin = open("01_input.txt")


T = int(input())


def check_x1(x, y, color):
    cnt = x
    flag = 0
    while cnt < N:
        cnt += 1
        if maps[y][cnt] == 0:
            break
        if maps[y][cnt] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y][x+1] == color:
            return
        maps[y][x+1] = color
        check_x1(x+1, y, color)

def check_x0(x, y, color):
    cnt = x
    flag = 0
    while cnt > 1:
        cnt -= 1
        if maps[y][cnt] == 0:
            break
        if maps[y][cnt] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y][x-1] == color:
            return
        maps[y][x-1] = color
        check_x0(x-1, y, color)


def check_y1(x, y, color):
    cnt = y
    flag = 0
    while cnt < N:
        cnt += 1
        if maps[cnt][x] == 0:
            break
        if maps[cnt][x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y+1][x] == color:
            return
        maps[y+1][x] = color
        check_y1(x, y+1, color)


def check_y0(x, y, color):
    cnt = y
    flag = 0
    while cnt > 1:
        cnt -= 1
        if maps[cnt][x] == 0:
            break
        if maps[cnt][x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y-1][x] == color:
            return
        maps[y-1][x] = color
        check_y0(x, y-1, color)


def check_x0y0(x, y, color):
    cnt_y = y
    cnt_x = x
    flag = 0
    while cnt_y > 1 and cnt_x > 1:
        cnt_y -= 1
        cnt_x -= 1
        if maps[cnt_y][cnt_x] == 0:
            break
        if maps[cnt_y][cnt_x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y-1][x-1] == color:
            return
        maps[y-1][x-1] = color
        check_x0y0(x-1, y-1, color)

def check_x1y1(x, y, color):
    cnt_y = y
    cnt_x = x
    flag = 0
    while cnt_y < N and cnt_x < N:
        cnt_y += 1
        cnt_x += 1
        if maps[cnt_y][cnt_x] == 0:
            break
        if maps[cnt_y][cnt_x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y+1][x+1] == color:
            return
        maps[y+1][x+1] = color
        check_x1y1(x+1, y+1, color)

def check_x0y1(x, y, color):
    cnt_y = y
    cnt_x = x
    flag = 0
    while cnt_y < N and cnt_x > 1:
        cnt_y += 1
        cnt_x -= 1
        if maps[cnt_y][cnt_x] == 0:
            break
        if maps[cnt_y][cnt_x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y+1][x-1] == color:
            return
        maps[y+1][x-1] = color
        check_x0y1(x-1, y+1, color)

def check_x1y0(x, y, color):
    cnt_y = y
    cnt_x = x
    flag = 0
    while cnt_y > 1 and cnt_x < N:
        cnt_y -= 1
        cnt_x += 1
        if maps[cnt_y][cnt_x] == 0:
            break
        if maps[cnt_y][cnt_x] == color:
            flag = 1
            break
    if flag == 1:
        if maps[y-1][x+1] == color:
            return
        maps[y-1][x+1] = color
        check_x1y0(x+1, y-1, color)




for case in range(1, T + 1):
    N, M = map(int, input().split())
    stone = []
    for m in range(M):
        stone.append(list(map(int, input().split())))

    maps = [[0 for x in range(N+1)] for y in range(N+1)]

    k = N//2
    maps[k][k] = 2
    maps[k+1][k+1] = 2
    maps[k+1][k] = 1
    maps[k][k+1] = 1
    for s in range(len(stone)):
        x = stone[s][0]
        y = stone[s][1]
        color = stone[s][2]
        maps[y][x] = color
        check_x0(x, y, color)
        check_x1(x, y, color)
        check_y0(x, y, color)
        check_y1(x, y, color)
        check_x0y0(x, y, color)
        check_x1y1(x, y, color)
        check_x0y1(x, y, color)
        check_x1y0(x, y, color)

    cnt_1 = 0
    cnt_2 = 0
    for y in range(N+1):
        for x in range(N+1):
            if maps[y][x] == 1:
                cnt_1 += 1
            elif maps[y][x] == 2:
                cnt_2 += 1
    print(cnt_1, cnt_2)

