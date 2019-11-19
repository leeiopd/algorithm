'''
철수는 자기 마을의 위성사진을 봤는데 평지와 언덕으로 나뉘어져 있음을 알았다.

위성사진이라서 언덕의 높이를 알 수 없어서 아쉬운 마음에 현지 조사를 통해 언덕의 높이를 알아낼 방법을 알아냈다.

언덕의 상하좌우에 한군데라도 평지가 있거나 마을 가장자리에 언덕이 위치해있다면 높이는 1m 이고 언덕의 상하좌우에 모두 언덕이 있다면 주변 언덕의 가장 낮은 언덕의 높이보다 1m 높아진다.
 
N*N 크기의 마을의 위성사진에는 평지는 0, 언덕은 1로 표시된다.

철수는 자기 마을 뿐 아니라 다른 마을의 위성사진을 분석해서 언덕의 높이를 구하고 싶어졌다.

당신은 철수를 도와 위성사진을 분석해서 가장 높은 언덕의 높이를 구하자.



첫 줄에는 마을 크기 (N,  1≤N≤100)가 주어진다.
다음 줄부터 N줄까지 마을의 위성사진 정보가 주어진다.

가장 높은 언덕 높이를 출력한다.

5
00100
01110
01110
01110
00100
'''

import sys

sys.stdin = open("B3_input.txt")

N = int(input())

maps = []
map0 = [0] * (N+2)
maps.append(map0)

for n in range(N):
    k = [0]
    p = (list(map(int, input())))
    k = k + p
    k.append(0)
    maps.append(k)
maps.append(map0)

def check(x, y):
    global maps
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    mins = 99
    cnt = 0
    if maps[y][x] >= 1:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if maps[Y][X] >= 1:
                cnt += 1
                if maps[Y][X] < mins:
                    mins = maps[Y][X]
    if cnt == 4:
        maps[y][x] = mins+1

cnt = 0
max_m = 0
while True:
    max_cnt = max_m
    cnt += 1
    for y in range(1, N+1):
        for x in range(1, N+1):
            check(x, y)
            if maps[y][x] > max_m:
                max_m = maps[y][x]
    if max_cnt == max_m:
        break

print(max_m)
