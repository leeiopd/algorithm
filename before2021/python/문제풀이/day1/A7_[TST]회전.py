'''
정사각형의 크기와 각 숫자를 입력 받은 후 시계방향으로 회전하는 프로그램을 작성하시오.
(1) 키보드를 통해 아래와 같은 크기 n과 각 행의 숫자를 입력 받는다. (<표>참고)
(2) 회전할 각도를 입력 받는다. (90, 180, 270, 360)
(3) 입력 받은 배열을 시계방향으로 입력 받은 각도만큼 회전하여 출력한다.
(4) 하나의 회전을 마친 후에는 회전된 데이터를 중심으로 다시 각도를 입력 받아서 회전한다.



첫 번째 줄에서 사각형의 크기 n(5≤n≤50)을 입력 받은 후 다음 줄부터 왼쪽 위 (1, 1)에서 오른쪽 아래 (n, n)까지

x, y 좌표 순서로 각 해당 좌표에 들어갈 숫자(9 이하의 자연수)를 입력 받는다. 여기서 말하는 x, y 란 (가로, 세로)를 의미한다.

다음 줄부터는 회전할 각도 (90, 180, 270, 360 중의 하나)를 입력 받는다.

하나의 결과가 나온 후에도 계속 새로운 각도를 입력 받다가, 0이 입력되면 종료한다.

각도의 크기가 주어진 범위를 벗어날 경우는 다시 입력 받는다.


5
3 4 1 2 3
2 3 4 5 6
2 3 4 6 7
1 7 6 5 4
6 8 9 3 4
90
180
270
360
0
'''
import sys

sys.stdin = open("A7_input.txt")


def turn(maps):
    global new_maps
    for y in range(N):
        for x in range(N):
            k = N - x - 1
            new_maps[y][k] = maps[x][y]
    return new_maps

def print_maps(maps):
    for n in range(N):
        result = ' '.join(map(str, maps[n]))
        print(result)


N = int(input())

maps = []
for n in range(N):
    maps.append(list(map(int, input().split())))

angle = 0
new_maps = [[ 0 for x in range(N)] for y in range(N)]
while True:
    new_angle = int(input())
    if new_angle == 0:
        break
    angle += new_angle

    

    if new_angle == 90:
        maps=turn(maps)
        new_maps = [[ 0 for x in range(N)] for y in range(N)]
        print_maps(maps)
    
    elif new_angle == 180:
        for i in range(2):
            maps=turn(maps)
            new_maps = [[ 0 for x in range(N)] for y in range(N)]
        print_maps(maps)
    
    elif new_angle == 270:
        for i in range(3):
            maps=turn(maps)
            new_maps = [[ 0 for x in range(N)] for y in range(N)]
        print_maps(maps)

    elif new_angle == 360:
        for i in range(4):
            maps=turn(maps)
            new_maps = [[ 0 for x in range(N)] for y in range(N)]
        print_maps(maps)

'''
6 1 2 2 3 
8 7 3 3 4 
9 6 4 4 1 
3 5 6 5 2 
4 4 7 6 3 
----
3 6 7 4 4 
2 5 6 5 3 
1 4 4 6 9 
4 3 3 7 8 
3 2 2 1 6 
---
4 3 9 8 6 
4 5 6 7 1 
7 6 4 3 2 
6 5 4 3 2 
3 2 1 4 3 
---
4 3 9 8 6 
4 5 6 7 1 
7 6 4 3 2 
6 5 4 3 2 
3 2 1 4 3 
'''