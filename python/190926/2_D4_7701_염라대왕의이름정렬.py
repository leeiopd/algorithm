'''
염라대왕은 이승의 사람들의 모든 이름을 가지고 있다.

어느날 저승에 일어난 진도 8.0 지진에 항상 정리되어 있던 이승 명부가 흐트러졌다.

이승 명부는 이름의 길이가 짧을수록 이 앞에 있었고, 같은 길이면 사전 순으로 앞에 있었다.

이왕 이렇게 된 김에 모든 이름을 다시 정리하고 같은 이름은 하나만 남겨놓기로 한 염라대왕을 도와주자.


[입력]

첫 번째 줄에 테스트 케이스의 수 T(1 ≤ T ≤ 50)가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 이승 명부의 이름 개수 N(1 ≤ N ≤ 20,000)이 주어진다.

각 테스트 케이스의 두 번째 줄부터 N개의 줄에 걸쳐서 알파벳 소문자로 이루어진 이름들이 주어진다.

이름에는 공백이 포함되지 않으며 최소 1개, 최대 50개의 알파벳으로 이루어져 있다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

정리된이름을한줄에하나씩출력하라.같은이름은한번만출력해야하는것을주의하라.
'''
import sys
sys.stdin = open('7701.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    nameList = []
    for n in range(N):
        name = input()
        K = len(name)
        nameList.append((K, name))
    nameList = list(set(nameList))
    nameList.sort()
    print('#{}'.format(case))
    for name in nameList:
        print(name[1])
