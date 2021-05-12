N = int(input())

wines = [0] * N
dp = [0] * N

for i in range(N):
    wines[i] = int(input())

dp[0] = wines[0]
if N > 1:
    dp[1] = wines[0] + wines[1]
# if N > 2:
#     dp[1] = wines[0] + wines[1]
for i in range(3, N):
    a = dp[i-1]
    b = wines[i] + dp[i-2]
    c = wines[i] + wines[i-1] + dp[i-3]

    print(i, a, b, c, dp[i-3])
    dp[i] = max(a, b, c)

print(dp[-1])