import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        f, t = map(int, sys.stdin.readline().split())
        graph[f][t] = 1
        graph[t][f] = 1

    isBipartite = True

    dq = deque()
    dq.append(1)
    visited = [0 for _ in range(V+1)]
    visited[1] = 1
    isBipartite = True
    while dq:
        f = dq.popleft()

        for t in range(1, V+1):
            if graph[f][t] and not visited[t]:
                visited[t] = -1 * visited[f]
                dq.append(t)
            elif graph[f][t] and visited[t] == visited[f]:
                isBipartite = False

    print("YES" if isBipartite else "NO")
