'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어

“3+(4+5)*6+7”

라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

"345+6*+7+"

변환된 식을 계산하면 64를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]

각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

# 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
'''
import sys
sys.stdin = open('1224.txt')

T = 1

for case in range(1, T+1):
    long = int(input())
    cals = input()
    nums = [str(x) for x in range(10)]
    change = [[] for x in range(10)]
    arithmetic = [[] for x in range(10)]
    level = 0
    numTemp = [[] for x in range(10)]
    Xflag = 0

    for cal in cals:
        if cal in nums:
            change[level].append(cal)

        if cal == '+':
            if Xflag == 1:
                while arithmetic[level]:
                    change[level].append(arithmetic[level].pop(0))
            Xflag = 0
            arithmetic[level].append(cal)

        if cal == '*':
            Xflag = 1
            temp = ['*']
            while arithmetic[level]:
                temp.append(arithmetic[level].pop(0))
            while temp:
                arithmetic[level].append(temp.pop(0))
        if cal == '(':
            level += 1
        if cal == ')':
            while arithmetic[level]:
                change[level].append(arithmetic[level].pop(0))
            while change[level]:
                change[level-1].append(change[level].pop(0))
            level -= 1

    while arithmetic[level]:
        change[level].append(arithmetic[level].pop(0))
    print(change)
    Ntemp = []
    for i in change[0]:
        if i in nums:
            Ntemp.append(int(i))
        if i == '+':
            a = Ntemp.pop(-1)
            b = Ntemp.pop(-1)
            c = a + b
            Ntemp.append(c)
        if i == '*':
            a = Ntemp.pop(-1)
            b = Ntemp.pop(-1)
            c = a * b
            Ntemp.append(c)
        print(Ntemp)
    print('#{} {}'.format(case, Ntemp[0]))
