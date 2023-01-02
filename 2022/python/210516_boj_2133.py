N = int(input())

dp = [0] * (N+2)
dp[0] = 1
dp[2] = 3

for i in range(4, N+1, 2):
    dp[i] = dp[i-2] + sum(dp[:i-1]) * 2
    
print(dp[N])