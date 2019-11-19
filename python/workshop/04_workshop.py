'''
수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.

어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.

[입력]

맨 첫 줄에는 테스트 케이스의 개수가 주어진다.

그리고 테스트 케이스가 각 라인에 주어진다. 각 테스트 케이스는 2줄로 구성되며, 첫 줄에는 원형 금속 막대의 개수 n이 주어지고, 다음 줄에는 2n개의 수가 주어진다.

숫자는 공백으로 구분한다. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미한다.

3
3 4 2 3 4 5
'''

import sys

sys.stdin = open('04_input.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    bolt_list = [[0 for _ in range(2)] for _ in range(N)]

    lists = list(map(int, input().split()))
    for n in range(len(lists)):
        i = n%2
        j = n//2
        bolt_list[j][i] = lists[n]

    for k in range(N):
        cnt = 0
        for j in range(N):
            if bolt_list[k][0] != bolt_list[j][1]:
                cnt -= 1
        if cnt == -N:
            break

    result = bolt_list[k]

    while len(result) < 2*N:
        for k in range(N):
            if result[-1] == bolt_list[k][0]:
                result = result + bolt_list[k]

    result = ' '.join(map(str, result))
    print(f'#{case} {result}')


