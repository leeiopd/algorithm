primes = [0, 0] + [1] * 1000

for i in range(2, 1001):
    if primes[i]:
        for j in range(i+i, 1001, i):
            primes[j] = 0

N = int(input())
nums = list(map(int, input().split()))
res = 0
for n in nums:
    if primes[n]:
        res += 1

print(res)
