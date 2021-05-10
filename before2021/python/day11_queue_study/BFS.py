node, line = 7, 8
maps = [[0 for x in range(8)]for y in range(8)]

route = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

route = list(map(int, route.split()))

half = len(route)//2

for i in range(half):
    x = route[i * 2]
    y = route[i * 2 + 1]
    maps[y][x] = 1
    maps[x][y] = 1


result = []
visited = [0] * 8


def BFS(maps, v):
    global visited, result
    queue = []
    queue.append(v)
    visited[v] += 1
    result.append(v)
    while queue:
        t = queue.pop(0)
        for i in range(len(maps[t])):
            if maps[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t]+1
                result.append(i)

BFS(maps, 1)
print(result)
print(visited[result[-1]]-1)