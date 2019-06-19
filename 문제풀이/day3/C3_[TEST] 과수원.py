'''
사과 과수원에서 밭을 열십자 모양으로 4등분하여 사과의 개수가 균등한 경우의 수를 구한다.
1은 사과이며 0은 사과가 없는 밭을 의미한다.
밭을 4등분하여 만들수 없는 경우는 -1을 출력한다.
다음은 균등하게 4등분한 경우의 예이다


N개가 주어지고 다음에 맵의 정보가 주어진다. (N은 최대 10)

4등분하여 사과의 개수가 균등한 경우의 수가 모두 몇가지인지를 구한다.
'''
import sys

sys.stdin = open("C3_input.txt")

N = int(input())

maps = []

for y in range(N):
    maps.append(list(map(int, list(input()))))
cnt  = 0
for point_y in range(1, N):
    for point_x in range(1, N):

        add1 = 0
        for y in range(point_y):
            for x in range(point_x):
                add1 += maps[y][x]

        add2 = 0
        for y in range(point_y, N):
            for x in range(point_x):
                add2 += maps[y][x]
        if add1 != add2:
            continue

        add3 = 0
        for y in range(point_y):
            for x in range(point_x, N):
                add3 += maps[y][x]
        if add1 != add3:
            continue

        add4 = 0
        for y in range(point_y, N):
            for x in range(point_x, N):
                add4 += maps[y][x]
        if add1 != add4:
            continue

        cnt += 1

if cnt == 0:
    print('-1')
else:
    print(cnt)