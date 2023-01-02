from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

res = 0

for i in range(1, N+1):
    for comb in combinations(range(N), i):
        add = 0
        for c in comb:
            add += nums[c]
        if add == S:
            res += 1
print(res)
