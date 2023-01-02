N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))
    
dp = [0] * N
dp[0] = nums[0]

if N > 1:
    dp[1] = nums[1] + nums[0]
    
if N > 2:
    dp[2] = max(nums[2]+nums[0], nums[2]+nums[1])
    
if N > 3:
    for i in range(3, N):
        a = nums[i] + nums[i-1] + dp[i-3]
        b = nums[i] + dp[i-2]
        dp[i] = max(a, b)

print(dp[-1])