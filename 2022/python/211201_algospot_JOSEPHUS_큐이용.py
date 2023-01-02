from collections import deque

C = int(input())

for _ in range(C):
    N, K = map(int, input().split())

    queue = deque([x+1 for x in range(N)])
    cnt = N
    while cnt > 2:
        cnt -= 1
        queue.popleft()

        for i in range(K-1):
            queue.append(queue.popleft())
    print(*queue)
