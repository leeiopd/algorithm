def DFS(V, N, maps):
    global DFSvisited
    DFSvisited.append(V)
    for i in range(1, N+1):
        if maps[V][i] and i not in DFSvisited:
            DFS(i, N, maps)


def BFS(V, N, maps):
    global BFSVisited
    queue = [V]
    BFSVisited = [V]

    while queue:
        f = queue.pop(0)
        for i in range(1, N+1):
            if maps[f][i] and i not in BFSVisited:
                queue.append(i)
                BFSVisited.append(i)


N, M, V = map(int, input().split())
maps = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    f, t = map(int, input().split())
    maps[f][t] = 1
    maps[t][f] = 1

DFSvisited = []
DFS(V, N, maps)
print(" ".join(map(str, DFSvisited)))

BFSVisited = []
BFS(V, N, maps)
print(" ".join(map(str, BFSVisited)))
