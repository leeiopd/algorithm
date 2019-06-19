'''
N×M장기판에 졸 한 개와 말 한 개가 놓여 있다. 말의 이동 방향이 다음과 같다고 할 때, 말이 최소의 이동횟수로 졸을 잡으려고 한다.


말이 졸을 잡기 위한 최소 이동 횟수를 구하는 프로그램을 작성해보자.

첫 줄은 장기판 행의 수(N)와 열의 수(M)를 받는다.(1≤N,M≤100)
둘째 줄은 말이 있는 위치의 행(R), 열(C)의 수와 졸이 있는 위치의 행(S), 열(K)의 수를 입력 받는다.
단, 장기판의 제일 왼쪽 위의 위치가 (1,1)이다.
각 행과 열은 R(1≤R≤N), C(1≤C≤M), S(1≤S≤N), K(1≤K≤M)이다.

말이 졸을 잡기 위한 최소 이동 횟수를 출력한다.
'''
import sys

sys.stdin = open("장기.txt")

N, M = map(int, input().split())

maps = [[0 for x in range(M+1)] for y in range(N+1)]

R, C, S, K = map(int, input().split())

cnt = 1
queue = [[C, R]]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

maps[R][C] = 0

while queue:
    x, y = queue.pop(0)

    for i in range(8):
        X = x + dx[i]
        Y = y + dy[i]

        if Y >= 1 and Y < N and X >= 1 and X < M :
            if maps[Y][X] != 0:
                continue
            if X == K and Y == S:
                result = maps[y][x]
                break
            maps[Y][X] = maps[y][x] + 1
            queue.append([X, Y])

print(result-1)