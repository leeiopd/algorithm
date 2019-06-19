'''
0이상 9이하의 숫자로 이뤄진 문자열 S가 주어졌을 때,
S 사이에 적당히 +기호를 추가 하여 주어진 정수 X에 대해 SA + SB = X 를 만족시키는 경우가 존재하는지 알아내는 프로그램을 작성하라.
여기서 SA는 추가된 +기호 앞, SB는 추가된 +기호 뒤의 문자열을 뜻한다. 예를 들어 S = "1245", X = 57일 경우 2와 4 사이에 +기호를 추가시켜 12+45=57을 만들 수 있다.

입력은 한 줄로 이뤄지며 길이 20 이하의 문자열 S와 1이상 1,000,000,000 이하의 정수 X가 입력된다.

입력에 대해 SA + SB = X를 만족하는 경우가 존재하면 “SA+SB=X”(괄호제외)의 형태로 출력한다.
만약 존재하지 않을 경우 "NONE"을 출력한다.
'''

import sys

sys.stdin = open("C0_input.txt")

S, X = map(str, input().split())

X = int(X)

num_l = len(S)
result = 0
for i in range(1, num_l):
    A = S[:i]
    B = S[i:]

    A_int = int(A)
    B_int = int(B)

    if A_int+B_int == X:
        result = 1
        break

if result == 1:
    A = str(A_int)
    B = str(B_int)
    print(A, end='')
    print('+', end='')
    print(B, end='')
    print('=', end='')
    print(X)

else:
    print('NONE')


