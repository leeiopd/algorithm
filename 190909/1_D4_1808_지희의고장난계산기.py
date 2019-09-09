'''
공대생인 지희는 계산기를 하나 가지고 있다.

그러나 이 계산기는 버튼이 많이 고장 나서 몇 개의 숫자 버튼과 곱하기 버튼, 그리고 계산 버튼밖에 남지 않았다.

지희는 숫자 X를 계산하고 싶다. 이를 위해서 눌러야 하는 최소 버튼 수를 구하고 싶다.

예를 들어, X=60이고 숫자 버튼을 ‘1’, ‘2’, ‘5’만 누를 수 있다고 하자. 다음과 같은 식으로 누르는 것이 다섯 번으로 최적이다.

“12”(두 번 누름) → 곱하기(한 번 누름) → “5”(한 번 누름) → 계산 (한 번 누름)

이번엔 X=4128 이고 숫자 버튼을 ‘6’, ‘8’만 누를 수 있다고 하자. 다음과 같은 식으로 누르는 것이 여섯 번으로 최적이다.

“688”(세 번 누름) → 곱하기(한 번 누름) → “6”(한 번 누름) → 계산 (한 번 누름)


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에 열 개의 정수가 공백으로 구분되어 주어진다.

주어지는 정수는 0 또는 1로, i번째 정수는 계산기에서 i-1를 누를 수 있는 버튼의 상태를 나타낸다. 1이면 동작함, 0이면 동작하지 않음이다.

두 번째 줄에는 하나의 정수 X(1 ≤ X ≤ 106)이 주어진다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

각 테스트 케이스마다 최소 몇 개의 버튼을 눌러야 X를 계산할 수 있는지 출력한다. 만약 불가능하면 -1을 출력한다.
'''
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1808.txt')

T = int(input())


def dfs(ans, cnt=1):
    global result
    print(X)
    if int(ans) > X:
        return
    if cnt >= result:
        return
    if int(ans) == X:
        if cnt < result:
            result = cnt
        return

    for b in btn:
        if cnt <= result - 1:
            dfs(ans+str(b), cnt+1)
            if b != 1:
                M = int(ans) * b
                if M < X:
                    dfs(str(M), cnt+2)


for case in range(1, T+1):
    nums = list(map(int, input().split()))
    X = int(input())
    btn = []
    result = 9999999999999999
    for n in range(10):
        if nums[n]:
            btn.append(n)
    btn = btn[::-1]
    for b in btn:
        if b != 0:
            dfs(str(b))
    print(result)
