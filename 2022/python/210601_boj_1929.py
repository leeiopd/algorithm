primes = [0, 0] + [1] * 1000001

for i in range(2, 1000001):
    if primes[i]:
        for j in range(i+i, 1000001, i):
            primes[j] = 0

A, B = map(int, input().split())

for i in range(A, B+1):
    if primes[i]:
        print(i)
