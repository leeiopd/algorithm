'''
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.

예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[제약사항]

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

글자 판은 무조건 정사각형으로 주어진다.

ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

가로, 세로 각각에 대해서 직선으로만 판단한다.

즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.
'''

import sys
sys.stdin = open("06_input.txt")

T = 10

def check(box):
    result = 0
    for i in range(100):
        for j in range(100):
            check_x = ''
            check_y = ''
            for t in range(j, 100):
                check_x = check_x + box[i][t]
                check_y = check_y + box[t][i]

                if result < len(check_x) and check_x == check_x[::-1]:
                    result = len(check_x)
                if result < len(check_y) and check_y == check_y[::-1]:
                    result = len(check_y)
            if 100-j < result:
                break
    return result

for t in range(1, T + 1):
    case = int(input())
    box = []
    for i in range(100):
        line_x = list(input())
        box.append(line_x)
    result = check(box)
    print(f'#{case} {result}')