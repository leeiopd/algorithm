import sys

sys.stdin = open("DFS재귀_input.txt")
V, E = map(int,input().split()) # V: 정점의 갯수, E : 인접 경로 input 개수

temp = list(map(int, input().split())) # 인접경로 input

G = [[0 for i in range(V+1)] for j in range(V+1)] # 입접행렬 표
visited = [0 for i in range(V+1)]

for i in range(0, len(temp), 2):
    y = temp[i]
    x = temp[i+1]
    G[y][x] = 1
    G[x][y] = 1

# for i in range(E):
#     G[temp[i * 2]][temp[i * 2 + 1]] = 1
#     G[temp[i * 2 + 1]][temp[i * 2]] = 1


for i in range(1, V+1):
    print(f"{i} {G[i]}")



visited = []
stack = []
result = []

def dfs(n):
    global G, visited
    visited.append(n)
    result.append(n)
    for i in range(1, V+1):
        if G[n][i] == 1 and i not in visited:
            dfs(i)

dfs(1)
print(result)

##
# visited = [0 for i in range(V+1)]
# def dfs_T2(v):
#     global G, visited, V
#     G2 = G
#     V2 = V
#     visited_2 = visited
#     visited_2[v] = 1
#     print(v, end=" ")

#     for w in range(1, V2+1):
#         if G2[v][w] == 1 and visited_2[w] == 0:
#             dfs_T2(w)

# print(dfs_T2(1))


##
# visited = [0 for i in range(V+1)]
# def dfs_T(v):
#     global G, visited, V
#     G1 = G
#     V1 = V
#     visited_1 = visited
#     s = []

#     s. append(v)
#     while len(s) != 0:
#         v = s.pop()
#         if visited_1[v] == 0:
#             visited_1[v] = 1
#             print(v, end=" ")
#             for w in range(1, V1+1):
#                 if G1[v][w] == 1 and visited_1[w] == 0:
#                     s.append(w)
# print(dfs_T(1))


