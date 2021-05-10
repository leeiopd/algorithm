'''
아래와 같이 모눈종이에 각각의 칸들이 칠해져 있는 그림이 있을 때 모눈종이에서 찾고 싶은 패턴의 모양이 몇 개가 있는지를 검사하려고 한다.

이 때, 찾고자 하는 모눈종이의 크기 M(0≤M≤100)과 패턴의 크기 P(0≤M≤100)은 주어진다.

첫 번째 줄에는 모눈종이이의 크기 M(0≤M≤100)이 주어진다.
두 번째 줄부터 M 줄까지는 모눈종이에 그린 그림을 칠한 칸은 1로, 칠하지 않은 칸은 0으로 모눈종이의 줄 별로 입력한다.
다음 줄에는 패턴의 크기 P(0≤P≤100)가 주어진다. 다음 줄부터 P개의 줄에 걸쳐 찾고 싶은 패턴의 모양이 주어진다. 모양이 있는 부분만 1 로 입력하고 나머지는 0으로 처리한다.

출력은 찾고 싶은 패턴의 모양이 모눈종이에 그린 그림에 몇 개가 있는지 그 개수를 출력한다.

10
0000000001
1110000000
0000001000
0000101000
1111111111
0000101000
0000001000
0000000000
1110000000
0000000001
3
100
111
100
'''
import sys

sys.stdin = open("B4_input.txt")

M = int(input())

maps = []

for m in range(M):
    maps.append(list(map(int, input())))

P = int(input())

part1 = []

for m in range(P):
    part1.append(list(map(int, input())))

part2 = [[0 for x in range(P)] for y in range(P)]
part3 = [[0 for x in range(P)] for y in range(P)]
part4 = [[0 for x in range(P)] for y in range(P)]


def turn(part_past, part_change):
    for y in range(P):
        for x in range(P):
            k = P-y-1
            part_change[x][k] = part_past[y][x]

turn(part1, part2)
turn(part2, part3)
turn(part3, part4)


def check1(start_y, start_x):
    check_list = [[0 for x in range(P)] for y in range(P)]

    for y in range(P):
        for x in range(P):
            check_list[y][x] = maps[y+start_y][x+start_x]
    
    if check_list == part1:
        return True
    else:
        return False

def check2(start_y, start_x):
    check_list = [[0 for x in range(P)] for y in range(P)]

    for y in range(P):
        for x in range(P):
            check_list[y][x] = maps[y+start_y][x+start_x]
    
    if check_list == part2:
        return True
    else:
        return False

def check3(start_y, start_x):
    check_list = [[0 for x in range(P)] for y in range(P)]

    for y in range(P):
        for x in range(P):
            check_list[y][x] = maps[y+start_y][x+start_x]
    
    if check_list == part3:
        return True
    else:
        return False

def check4(start_y, start_x):
    check_list = [[0 for x in range(P)] for y in range(P)]

    for y in range(P):
        for x in range(P):
            check_list[y][x] = maps[y+start_y][x+start_x]
    
    if check_list == part4:
        return True
    else:
        return False
            


cnt = 0
for start_y in range(0, M-P+1):
    for start_x in range(0, M-P+1):
        if check1(start_y, start_x):
            cnt += 1
        if check2(start_y, start_x):
            cnt += 1
        if check3(start_y, start_x):
            cnt += 1
        if check4(start_y, start_x):
            cnt += 1

print(cnt)