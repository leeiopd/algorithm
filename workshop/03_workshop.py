'''
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

'''


import sys

sys.stdin = open("03_input.txt", "r")

T = 10

for i in range(T):
    # case input
    case = int(input())

    # input list 만들기
    mylist = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        mylist[i] = list(map(int, input().split()))

    max_add = 0

    # 가로줄 sum
    for x in range(100):
        add = 0
        for y in range(100):
            add += mylist[x][y]
        if max_add < add:
            max_add = add

    # 세로줄  sum
    for x in range(100):
        add = 0
        for y in range(100):
            add += mylist[y][x]
        if max_add < add:
            max_add = add

    # x == y 좌표 sum
    for x in range(100):
        add = 0
        for y in range(100):
            if x == y:
                add += mylist[x][y]
        if max_add < add:
            max_add = add

    # x + y = 99 좌표 sum
    for x in range(100):
        for y in range(100):
            if x + y == 99:
                add += mylist[x][y]
        if max_add < add:
            max_add = add

    print(f'#{case} {max_add}')