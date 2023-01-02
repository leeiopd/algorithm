import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

i = len(coins) - 1
res = 0
while K:
    if K < coins[i]:
        i -= 1
        continue
    res += K // coins[i]
    K = K % coins[i]

print(res)
