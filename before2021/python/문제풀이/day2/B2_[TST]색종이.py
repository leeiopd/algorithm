'''
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.

이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.

이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 둘레의 길이를 구하는 프로그램을 작성하시오.
 
예를 들어 흰색 도화지 위에 네 장의 검은색 색종이를 <그림 1>과 같은 모양으로 붙였다면 검은색 영역의 둘레는 96 이 된다.


첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고,
두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다.
색종이의 수는 100이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다.

첫째 줄에 색종이가 붙은 검은 영역의 둘레의 길이를 출력한다.

4
3 7
5 2
15 7
13 14
'''
import sys

sys.stdin = open("B2_input.txt")

K = int(input())
N = 100

maps = [ [ 0 for x in range(105)] for y in range(105) ]

def check(x, y):
    global maps
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if maps[Y][X] == 1:
            cnt  += 1
    return cnt

for n in range(K):
    point_x, point_y  = map(int, input().split())
    for y in range(N-point_y-8, N-point_y+2):
        for x in range(1+point_x, 1+point_x + 10):
            maps[y][x] = 1
cnt = 0
for y in range(1, N+2):
    for x in range(1, N+2):
        if maps[y][x] == 0:
            cnt += check(x, y)



result = cnt
print(result)