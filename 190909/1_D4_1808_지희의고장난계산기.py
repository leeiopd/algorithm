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


# 버튼으로 만들수 있는 숫자 리스트 생성
def makeNumFunc(num=0, cnt=0):
    if num > X:
        return
    if cnt > 7:
        return
    for i in nums:
        N = num + i
        if N:
            madeNums.append(N)
            makeNumFunc(N*10, cnt+1)

# 만들어진 숫자 리스트로 X에 나누면서 결과 뽑기


def findAns(A, cnt=0):
    global result
    # 주어진 X 가 1이어서 cnt == 0 일때의 상황을 방지
    if cnt and A == 1:
        if cnt < result:
            result = cnt
            return
    for i in range(len(madeNums)-1, -1, -1):
        # 1로 계속 나누는 상황 방지 stack over flow // 큰 수들로 나누는 상황 방지 // 나눌수 있는 수인지 확인
        if madeNums[i] != 1 and madeNums[i] <= A and A % madeNums[i] == 0:
            K = len(str(madeNums[i]))
            findAns(A//madeNums[i], cnt+K+1)


for case in range(1, T+1):
    btn = list(map(int, input().split()))
    X = int(input())
    nums = []
    for b in range(len(btn)):
        if btn[b]:
            nums.append(b)

    madeNums = []
    makeNumFunc()
    madeNums.sort()

    # 주어진 X가 버튼을 눌러서 나오는 숫자인지 확인
    if X in madeNums:
        result = len(str(X))+1
    else:
        result = 9999999

    findAns(X)

    if result == 9999999:
        result = -1
    print('#{} {}'.format(case, result))
