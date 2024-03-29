# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
# 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

visited = [0] * N
res = 123456789

add = 0


def DFS(f, add, visited):
    global res
    if add > res:
        return
    if sum(visited) == N-1:
        if maps[f][0]:
            res = min(res, add+maps[f][0])
        return

    for i in range(1, N):
        if maps[f][i] and visited[i] == 0:
            visited[i] = 1
            DFS(i, add+maps[f][i], visited)
            visited[i] = 0


for i in range(1, N):
    if maps[0][i]:
        visited[i] = 1
        DFS(i, maps[0][i], visited)
        visited[i] = 0

print(res)
