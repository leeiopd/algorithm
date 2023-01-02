from collections import deque


def makePrime():
    nums = [1] * 10000
    nums[0] = 0
    nums[1] = 0

    for i in range(2, 10000):
        if nums[i]:
            for j in range(i, 10000, i):
                if i == j:
                    continue
                nums[j] = 0
    return nums


primes = makePrime()

case = int(input())

for _ in range(case):
    A, B = map(int, input().split())
    if A == B:
        print(0)
        continue
    if A > B:
        A, B = B, A

    queue = deque()
    queue.append(A)

    check = [0] * 10000
    check[A] = 1

    while True:
        Q = queue.popleft()

        if Q == B:
            print(check[Q]-1)
            break

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                nextQ = list(str(Q))
                nextQ[i] = str(j)
                nextQ = int("".join(nextQ))

                if primes[nextQ] and not check[nextQ]:
                    check[nextQ] = check[Q] + 1
                    queue.append(nextQ)
