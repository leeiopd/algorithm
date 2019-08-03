'''
숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.

이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.


[출력]

각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.
'''
import sys
sys.stdin = open('5948.txt')

T = int(input())


for case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    resultList = []
    for n in range(5):
        for m in range(n, 6):
            for l in range(m, 7):
                tmp = nums[n] + nums[m] + nums[l]
                if tmp not in resultList:
                    resultList.append(tmp)
    print(sorted(resultList)[-5])
