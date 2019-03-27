'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.

N = 0.625
0.101 (이진수)
= 1*2-1 + 0*2-2 + 1*2-3
= 0.5 + 0 + 0.125
= 0.625

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.
'''

import sys

sys.stdin = open("02_input.txt")

T = int(input())
for case in range(1, T+1):
    N = float(input())
    result = ''
    while N:
        if len(result) >12:
            result = 'overflow'
            break
        N *= 2
        int_N = int(N)
        N -= int_N
        if int_N == 1:
            result += '1'
        else:
            result += '0'

    print(f'#{case} {result}')