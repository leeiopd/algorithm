N = int(input())

dp = [ i for i in range(N+1)]

for i in range(1, N+1):
    tmp = []
    for j in range(1, i):
        if j*j > i:
            break
        tmp.append(dp[i - j*j])
    if tmp:
        dp[i] = min(tmp) + 1
        
print(dp[N])