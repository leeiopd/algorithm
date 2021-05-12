import copy
N = int(input())

nums = list(map(int, input().split()))
dp = [0] * N
dp = copy.deepcopy(nums)

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+nums[i], dp[i])
print(max(dp))