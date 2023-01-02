import sys
from collections import deque

input = sys.stdin.readline
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)

    node = [0] * (V+1)
    isBipartite = True

    for v in range(1, V+1):
        if not isBipartite:
            break
        if not node[v]:
            node[v] = 1

            dq = deque()
            dq.append(v)

            while dq:
                f = dq.popleft()

                for t in graph[f]:
                    if not node[t]:
                        node[t] = node[f] * -1
                        dq.append(t)
                    elif node[t] == node[f]:
                        isBipartite = False
                        break
    print("YES" if isBipartite else "NO")
