import sys


def countGraph(N, graph):
    if N == 1:
        return 1
    visited = []
    res = 0
    for n in range(1, N+1):
        if n not in visited:
            res += 1
            queue = [n]

            while queue:
                f = queue.pop(0)
                visited.append(f)
                for t in range(1, N+1):
                    if graph[f][t] and t not in visited:
                        queue.append(t)
                        visited.append(t)
    return res


N, M = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1


print(countGraph(N, graph))
