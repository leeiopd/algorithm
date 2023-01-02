from collections import deque

C = int(input())


def makeSignal(N, K):
    queue = deque()
    queue.append(1983)
    add = 1984
    result = 0
    tmp = 0

    for i in range(N + 1):
        if add == K:
            result += 1

        if len(queue):
            sig = (queue[-1] * 214013 + 2531011) % (2 ** 32)
        else:
            sig = (tmp * 214013 + 2531011) % (2 ** 32)
        queue.append(sig)
        add += sig % 10000 + 1

        while add > K:
            tmp = queue[-1]
            s = queue.popleft()
            add -= s % 10000 + 1
    return result


for _ in range(C):
    K, N = map(int, input().split())
    result = makeSignal(N, K)
    print(result)
