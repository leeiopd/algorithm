from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

parent = [0] * (N+1)


dq = deque()
dq.append(1)

while dq:
    n = dq.popleft()

    for m in graph[n]:
        if not parent[m]:
            parent[m] = n
            dq.append(m)


for p in parent[2:]:
    print(p)
