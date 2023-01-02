N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
dp[1] = [1 for _ in range(N+1)]

for k in range(2, K+1):
    dp[k][1] = k

for k in range(2, K+1):    
    for n in range(2, N+1):
        dp[k][n] = dp[k-1][n] + dp[k][n-1]
        
print(dp[K][N]%1000000000)