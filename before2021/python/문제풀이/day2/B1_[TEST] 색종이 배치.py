'''
색종이 2장을 주어진 시작좌표와 크기로 도화지에 배치하려 한다.
2장의 색종이를 배치하면 다음과 같은 4가지 유형으로 배치가 된다.
그럼 다음의 4가지 유형중에서 어떤 모양으로 배치 되는지 유형의 번호를 출력한다.


줄단위로 색종이의 시작 행, 열 좌표와 가로, 세로 크기가 각각 주어진다.(맵 크기는 최대 100이내)

4가지 유형중 어떤 유형으로 배치되는지를 구한다.

2 3 4 4
6 7 4 4
'''

import sys

sys.stdin = open("B1_input.txt")

maps = [[0 for x in range(30)] for y in range(30)]

start_x1, start_y1, x1_long, y1_long = map(int, input().split())
start_x2, start_y2, x2_long, y2_long = map(int, input().split())

result = 4

for y in range(start_y1, start_y1 + y1_long):
    for x in range(start_x1, start_x1 + x1_long):
        maps[y][x] += 1

for y in range(start_y2, start_y2 + y2_long):
    for x in range(start_x2, start_x2 + x2_long):
        maps[y][x] += 1


if maps[start_y1 + y1_long][start_x1 + x1_long] == 1:
    result = 1
elif maps[start_y1 - 1 ][start_x1 + x1_long ] == 1:
    result = 1
elif maps[start_y1 - 1][start_x1 - 1 ] == 1:
    result = 1
elif maps[start_y1 + y1_long][start_x1 - 1 ] == 1:
    result = 1




for y in range(start_y1, start_y1 + y1_long):
    if maps[y][start_x1-1] == 1:
        result = 2
    elif maps[y][start_x1 + x1_long] == 1:
        result = 2

for x in range(start_x1, start_x1 + x1_long):
    if maps[start_y1 - 1][x] == 1:
        result = 2
    elif maps[start_y1 + y1_long][x] == 1:
        result = 2

for y in range(30):
    for x in range(30):
        if maps[y][x] == 2:
            result = 3
print(result)



