'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

'''

import sys

sys.stdin = open("3_input.txt")

N = int(input())

maps = [[0 for x in range(N+2)]]

for n in range(N):
    x_line = [0] + list(map(int, input())) + [0]
    maps.append(x_line)
maps.append([0 for x in range(N+2)])


def find_house(x, y):
    global mpas, cnt, house_cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if maps[Y][X] == 1:
            maps[Y][X] = cnt
            house_cnt += 1
            find_house(X, Y)

cnt = 1
result = []
for y in range(N+2):
    for x in range(N+2):
        if maps[y][x] == 1:
            cnt += 1
            house_cnt = 1
            find_house(x, y)
            result.append(house_cnt)

result.sort()
print(cnt-1)
for r in result:
    if r != 1:
        print(r-1)
    else:
        print(r)