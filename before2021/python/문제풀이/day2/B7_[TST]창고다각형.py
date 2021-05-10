'''
N개의 막대 기둥이 일렬로 세워져 있다. 기둥들의 폭은 모두 1m이며 높이는 다를 수 있다.
이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다. 창고에는 모든 기둥이 들어간다. 이 창고의 지붕을 다음과 같이 만들다.
 
(1) 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
(2) 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
(3) 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
(4) 지붕의 가장자리는 땅에 닿아야 한다.
(5) 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.
 
그림 1은 창고를 옆에서 본 모습을 그린 것이다.
이 그림에서 굵은 선으로 표시된 부분이 지붕에 해당 되고, 지붕과 땅으로 둘러싸인 다각형이 창고를 옆에서 본 모습이다.
이 다각형을 창고 다각형이라고 하자.

첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다.
N은 1이상 1,000 이하 이다.
그 다음 N개의 줄에는 각 줄의 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다.
L과 H는 둘 다 1 이상 1,000 이하 이다.

첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.

7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
import sys

sys.stdin = open("B7_input.txt")

N = int(input())

maps = [ [0 for x in range(1003)] for y in range(1001)]
max_h = 0
box_list = [0] * 1002
for n in range(N):
    l, h = map(int, input().split())
    if max_h < h:
        max_h = h
        max_x = l
    box_list[l] = h

high = 0
for x in range(max_x):
    if box_list[x] > high:
        high = box_list[x]
    else:
        box_list[x] = 0

high = 0
for x in range(1001, max_x, -1):
    if box_list[x] > high:
        high = box_list[x]
    else:
        box_list[x] = 0



def start1(box_list):
    for x in range(max_x):
        if box_list[x] != 0:
            return x
    return 0

def start2(box_list):
    for x in range(1001, max_x, -1):
        if box_list[x] != 0:
            return x
    return 1000


x = start1(box_list)
while True:
    if x == max_x+1:
        break
    if box_list[x] == 0:
        x += 1
        continue
    
    high_y = 1000 - box_list[x]

    for y in range(high_y+1, 1001):
        for i in range(x, max_x+1):
            maps[y][i] = 1
    x += 1

x = start2(box_list)
while True:
    if x == max_x:
        break
    if box_list[x] == 0:
        x -= 1
        continue
    
    high_y = 1000 - box_list[x]

    for y in range(high_y+1, 1001):
        for i in range(x, max_x-1, -1):
            maps[y][i] = 1
    x -= 1


cnt = 0
for y in range(1001):
    for x in range(1003):
        if maps[y][x] == 1:
            cnt += 1


print(cnt)