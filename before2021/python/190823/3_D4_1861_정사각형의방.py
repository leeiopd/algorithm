'''
N2개의 방이 N×N형태로 늘어서 있다.

위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며, 이 숫자는 모든 방에 대해 서로 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.

다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.

Ai, j는 모두 서로 다른 수이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을 이동할 수 있는지를 공백으로 구분하여 출력한다.

이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


[예제 풀이]

첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.

두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.
'''
import sys
sys.stdin = open('1861.txt')

T = int(input())


def DFS(x, y, deep=1):
    global tmp
    if deep > tmp:
        tmp = deep
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < N and 0 <= Y < N:
            if maps[y][x] + 1 == maps[Y][X]:
                DFS(X, Y, deep+1)


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for case in range(1, T+1):
    N = int(input())
    maps = []
    for n in range(N):
        maps.append(list(map(int, input().split())))

    result = 0
    room = -1
    for y in range(N):
        for x in range(N):
            tmp = 0
            DFS(x, y)
            if tmp > result:
                result = tmp
                room = maps[y][x]
            if tmp == result:
                if room > maps[y][x]:
                    room = maps[y][x]
    print('#{} {} {}'.format(case, room, result))
