'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("04_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n_count, l_count = map(int, input().split())
    nums = list(map(int, input().split()))

    # 기준이 될 첫구간 합
    add = 0
    for n in range(l_count):
        add += nums[n]

    # 최소값 최대값의 기준을 첫구간 합으로 시작.
    min_add = add
    max_add = add

    # 구간 길이
    l_side = l_count - 1

    # 한칸씩 이동하며 구간이 지나온 칸을 빼고 새로 받은 칸을 더하기,
    # 최대값 최소값 비교 결정.
    for i in range(1, len(nums) - l_side):
        add = add - nums[i-1] + nums[i+l_side]

        if max_add < add:
            max_add = add
        elif min_add > add:
            min_add = add

    result = max_add - min_add
    print(f'#{test_case} {result}')
