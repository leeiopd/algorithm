import sys
from itertools import combinations
import math

T = int(sys.stdin.readline())

for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    combi = list(combinations(nums[1:], 2))
    res = 0
    for com in combi:
        res += math.gcd(com[0], com[1])

    print(res)
