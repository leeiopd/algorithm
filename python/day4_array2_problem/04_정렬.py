'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.


10 1 9 2 8 3 7 4 6 5


주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
'''

import sys

sys.stdin = open("04_input.txt")

T = int(input())
for case in range(1, T+1):

    N = int(input()) # 정수의 갯수
    ai = list(map(int, input().split())) # N개 정수 list

    for n in range(N):
        min_index = n
        for a in range(n+1, N):
            if ai[min_index] > ai[a]:
                min_index = a
        ai[n], ai[min_index] = ai[min_index], ai[n]

    result = [0]*10

    for n in range(5):
        result[n*2] = ai[N-n-1]
        result[n*2+1] = ai[n]

    result = ' '.join(map(str,result))
    print(f'#{case} {result}')
