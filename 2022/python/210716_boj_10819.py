from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
res = 0
for per in permutations(range(N), N):
    tmp = 0
    for i in range(1, N):
        tmp += abs(nums[per[i]] - nums[per[i-1]])
    res = max(res, tmp)
print(res)
