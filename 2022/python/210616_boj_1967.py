import sys
from collections import deque


def BFS(start, finish=0):
    global N

    dq = deque()
    dq.append((start, 0))

    visited = [0] * (N+1)

    res = 0
    maxNode = 0

    while dq:
        f, add = dq.popleft()
        visited[f] = 1

        if finish and f == finish:
            return add

        for info in tree[f]:
            if visited[info[0]]:
                continue

            if res < add+info[1]:
                res = add + info[1]
                maxNode = info[0]
            dq.append((info[0], add+info[1]))

    return maxNode


input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    r, c, l = map(int, input().split())
    tree[r].append((c, l))
    tree[c].append((r, l))

v = BFS(1)
e = BFS(v)

print(BFS(v, e))
