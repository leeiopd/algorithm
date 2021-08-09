import sys
from itertools import combinations

input = sys.stdin.readline
while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    for comb in combinations(range(1, nums[0]+1), 6):
        for c in comb:
            print(nums[c], end=" ")
        print()
    print()
