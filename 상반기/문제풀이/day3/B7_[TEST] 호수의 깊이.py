'''
물과 육지로 표시된 호수 지도를 가지고 1인 물의 자리마다 물의 깊이를 구하고자 한다.
물은 1, 육지는 0으로 표시된다.
각 물의 위치마다 물의 깊이는 지도에서 물이 있는 각 칸이 육지로부터 떨어진 거리의 합과 일치한다.
단, 각 칸이 육지로부터 떨어진 거리는 동서남북의 거리 중 가장 짧은 거리이다.
모든 물은 육지로 둘러 쌓여 있다.

0 0 0 0 0 0
0 1 1 0 0 0
0 1 1 1 1 0
0 1 1 1 1 0
0 0 1 1 0 0
0 0 0 0 0 0

호수안에서 물의 깊이를 계산하면 다음과 같다.
6*6 지도에서 2만큼 떨어진 칸이 3개이고 1만큼 떨어진 칸이 9개이므로
이 호수의 전체 물의 깊이를 모두 합한 결과가 15가 된다.
0 0 0 0 0 0
0 1 1 0 0 0
0 1 2 1 1 0
0 1 2 2 1 0
0 0 1 1 0 0
0 0 0 0 0 0

맵의 크기 N이 주어지고 호수의 정보가 주어진다.(5<=N<=10)

이 호수에서 전체 물 깊이의 합을 구한다.

6
0 0 0 0 0 0
0 1 1 0 0 0
0 1 1 1 1 0
0 1 1 1 1 0
0 0 1 1 0 0
0 0 0 0 0 0
'''

import sys

sys.stdin = open("B7_input.txt")

N = int(input())

d = [1, -1]

def check(x, y):
    x0 = x
    x1 = x
    y0 = y
    y1 = y
    cnt_x0 = 0
    cnt_x1 = 0
    cnt_y0 = 0
    cnt_y1 = 0
    for n in range(N):
        x0 -= 1
        if x0 > 0 and maps[y][x0] != 0:
            cnt_x0 += 1
        elif x0 > -1 and maps[y][x0] == 0:
            cnt_x0 += 1
            return cnt_x0

        x1 += 1
        if x1 < N and maps[y][x1] != 0:
            cnt_x1 += 1
        elif x1 < N and maps[y][x1] == 0:
            cnt_x1 += 1
            return cnt_x1

        y0 -= 1
        if y0 > 0 and maps[y0][x] != 0:
            cnt_y0 += 1
        elif y0 > -1 and maps[y0][x] == 0:
            cnt_y0 += 1
            return cnt_y0

        y1 += 1
        if y1 < N and maps[y1][x] != 0:
            cnt_y1 += 1
        elif y1 < N and maps[y1][x] == 0:
            cnt_y1 += 1
            return cnt_y1



maps = []

for n in range(N):
    maps.append(list(map(int, input().split())))

for y in range(N):
    for x in range(N):
        if maps[y][x] != 0:
            cnt = check(x, y)
            maps[y][x] = cnt
add = 0
for y in range(N):
    for x in range(N):
       add += maps[y][x]

print(add)

