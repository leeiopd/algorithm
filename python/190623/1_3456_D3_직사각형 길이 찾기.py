"""
직사각형의 네 변 중에서 세 변의 길이가 주어진다.

나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.

세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.

입력으로 직사각형이 불가능한 경우는 주어지지 않는다.


다음 그림의 예시는 각각 a = 4, b = 3, c = 4의 입력과 a = 5, b = 5, c = 5의 입력을 받았을 때 직사각형의 모습이다.

빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 자연수 a, b, c(1 ≤ a, b, c ≤ 100)가 공백으로 구분되어 주어진다.


[출력]

각 테스트 케이스마다 나머지 한 변의 길이를 출력한다.
"""
import sys

sys.stdin = open("3456.txt")

T = int(input())

for case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[1] == nums[0]:
        result = nums[2]

    elif nums[1] == nums[2]:
        result = nums[0]

    else:
        result = nums[1]

    print(f"#{case} {result}")