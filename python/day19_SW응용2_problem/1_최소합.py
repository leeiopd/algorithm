'''
그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''

import sys

sys.stdin = open("1_input.txt")

T = int(input())


def check(x, y):
    if x > N-1:
        return 0
    if y > N-1:
        return 0
    return 1

def game(x, y, cnt):
    global result
    if x == N-1 and y == N-1:
        if result > cnt:
            result = cnt
        return

    dx = [1, 0]
    dy = [0, 1]

    for i in range(2):
        X = x + dx[i]
        Y = y + dy[i]
        if check(X, Y):
            cnt += maps[Y][X]
            if cnt > result:
                cnt -= maps[Y][X]
                continue
            game(X, Y, cnt)
            cnt  -= maps[Y][X]




for case in range(1, T+1):
    N = int(input())
    maps = []
    for n in range(N):
        maps.append(list(map(int, input().split())))
    cnt = maps[0][0]
    result = 99999999999999
    game(0, 0, cnt)
    print("#{} {}" .format(case, result))