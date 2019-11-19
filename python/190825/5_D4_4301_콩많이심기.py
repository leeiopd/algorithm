'''
콩을 사랑하는 민석이의 취미는 n*m 크기의 사각형 밭에 콩을 늘어놓는 것이다.

한 칸에 콩 하나씩을 놓을 수 있는데, 2가 싫은 민석이는 콩들 사이의 길이가 2가 되지 않도록 하면서 최대한 많은 콩을 놓으려고 한다.

예를 들어 다음과 같이 콩을 배치할 수 없다.



콩1(x1, y1)과 콩2(x2, y2) 사이의 길이는



이다.

민석이를 도와서 사각형 밭에 최대로 콩을 늘어놓자.


[입력]

첫째 줄에 테스트 케이스의 수 T (1 ≤ T ≤ 10)가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 가로길이 N, 세로길이 M이 주어진다.

(1 ≤ N, M ≤ 1000)

[출력]

각 테스트 케이스마다 밭에 놓을 수 있는 콩의 최대 개수를 출력하라.

[HINT]

3*2 밭에 콩을 배치하는 경우 다음과 같이 최대 4개를 배치할 수 있다.
'''
import sys
sys.stdin = open('4301.txt')

T = int(input())


# 콩이 심어진곳에서 두칸 거리에 있는 곳의 콩을 뽑아준다
def none(x, y):
    for i in range(4):
        X = x + cx[i]
        Y = y + cy[i]
        if 0 <= X < N and 0 <= Y < M:
            maps[Y][X] = 0


cx = [0, 0, 2, -2]
cy = [-2, 2, 0, 0]
for case in range(1, T+1):
    N, M = map(int, input().split())

    # 일단 콩을 모든곳에 심는다
    maps = [[1 for x in range(N)] for y in range(M)]

    # 심어진 콩에 대해 못심는 곳을 체크
    for y in range(M):
        for x in range(N):
            if maps[y][x]:
                none(x, y)

    result = 0
    for y in range(M):
        for x in range(N):
            if maps[y][x]:
                result += 1

    print('#{} {}'.format(case, result))
