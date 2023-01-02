# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 2
import sys

primes = [0, 0] + [1] * 1000000

for i in range(2, 1000001):
    if primes[i]:
        if i % 2 == 0:
            primes[i] = 0
            continue
        for j in range(i+i, 1000001, i):
            if primes[j]:
                primes[j] = 0

while True:
    N = int(sys.stdin.readline())
    if not N:
        break
    B = N-1
    A = 1
    while True:
        B -= 1
        A += 1

        if primes[B] and primes[A]:
            print(f"{N} = {A} + {B}")
            break
