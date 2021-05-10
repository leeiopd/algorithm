'''
창용 마을에는 N명의 사람이 살고 있다.

사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.

두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.

두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,

이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.

창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수를 나타내는

두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.

이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.

같은 관계는 반복해서 주어지지 않는다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

무리의 개수를 출력한다.
'''
import sys
sys.stdin = open('7465.txt')

T = int(input())


def dfs(n):
    # visited에 그룹을 표기
    visited[n] = cnt
    for i in range(N+1):
        # 알고 있는 사이이고 그룹이 표기되지 않으면 dfs 진행
        if maps[n][i] == 1 and visited[i] == 0:
            dfs(i)


for case in range(1, T+1):
    N, M = map(int, input().split())
    maps = [[0 for x in range(N+1)] for y in range(N+1)]

    for n in range(1, N+1):
        if n:
            maps[n][n] = 1

    for m in range(M):
        A, B = map(int, input().split())
        maps[A][B] = 1
        maps[B][A] = 1

    # visited 아이디어로 runtime error 해결
    # 처음 시도는 temp에 append로 담아가며 비교 하였는데
    # visited에 cnt를 표시하여 그룹을 나눌수 있었음
    visited = [0] * (N+1)
    cnt = 0
    for n in range(1, N+1):
        # 그룹이 표기되지 않았으면 그룹표기 숫자를 증가 시키고 진행
        if visited[n] == 0:
            cnt += 1
            dfs(n)
    print('#{} {}'.format(case, cnt))
