T = int(input())

for _ in range(T):
    N = int(input())
    
    dp = [0, 1, 2, 4] + [0] * N
    
    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])