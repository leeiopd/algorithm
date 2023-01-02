import sys
from collections import deque
input = sys.stdin.readline


def BFS(start, finish=0):
    global N

    dq = deque()
    dq.append((start, 0))

    res = [0, 0]
    visited = [0] * (N+1)

    while dq:
        f, add = dq.popleft()
        visited[f] = 1

        for info in graph[f]:
            t = info[0]
            l = info[1]

            if t == finish:
                return add+l

            if visited[t]:
                continue

            if res[1] < add + l:
                res = [t, add+l]

            dq.append((t, add+l))

    return res[0]


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    ins = list(map(int, input().split()))

    cnt = 1
    while True:
        if ins[cnt] == -1:
            break

        if not cnt % 2:
            graph[ins[0]].append((ins[cnt-1], ins[cnt]))
        cnt += 1

u = BFS(1)
v = BFS(u)

print(BFS(u, v))
