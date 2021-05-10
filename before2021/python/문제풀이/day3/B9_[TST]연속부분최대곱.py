'''
N개의 양의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아,
그 곱을 출력하는 프로그램을 작성하시오. 예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,

색칠된 부분의 곱이 최대가 되며, 그 값은 1.638이다.
결과는 double형의 범위를 넘지 않는다.

첫째 줄은 나열된 양의 실수들의 개수 N이 주어지고, 그 다음 줄부터 N개의 수가 한 줄에 하나씩 들어 있다.
N은 10,000 이하의 자연수이다.

계산된 최대값을 소수점 이하 넷째 자리에서 반올림하여 소수점 이하 셋째 자리까지 출력한다.
'''

import sys

sys.stdin = open("B9_input.txt")

N = int(input())

nums = []

for n in range(N):
    nums.append(float(input()))

result = 0
for start in range(N-1):
    product = 1
    for i in range(start, N):
        if nums[i] == 0:
            break
        product = product * nums[i]
        if product > result:
            result = product


print('%.3f'%result)
