'''
기지국위치에서 원안에 모든 마을을 포함하는 반경을 구하시오.(1은 마을 2는 기지국(기지국은 1개만 존재한다)
N*N(N은 1~10)의 맵의 크기가 주어진다. 최대반경은 1~13이내이다.
반경을 계산하는 수식은 d^2==(x2-x1)^2 + (y2-y1)^2 이다.

N을 입력받고 다음줄부터 맵의 정보가 주어진다.

원안의 마을을 모두 포함하는 반경(반지름)을 구하시오
'''

import sys

sys.stdin = open("C8_input.txt")


N = int(input())

maps = []

for y in range(N):
    maps.append(list(map(int, list(input()))))

for y in range(N):
    for x in range(N):
        if maps[y][x] == 2:
            check_x = x
            check_y = y
result = 0
for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:
            long_x = abs(check_x - x)
            long_y = abs(check_y - y)
            maxs = (long_x * long_x) + (long_y * long_y)
            if maxs > result:
                result = maxs
result = result ** (0.5)
int_result = int(result)

if result - int_result:
    print(int_result + 1)
else:
    print(int_result)