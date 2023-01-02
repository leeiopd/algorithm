import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

maps = []

for _ in range(N):
    maps.append(input().rstrip())

word = input().rstrip()

visited = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]


def DFS(y, x, idx):
    global N, M, K, word

    if visited[y][x][idx] != -1:
        return visited[y][x][idx]

    if maps[y][x] != word[idx]:
        return 0

    if idx == len(word)-1:
        return 1

    cnt = 0
    for i in range(-K, K+1):
        if not i:
            continue
        if 0 <= y+i < N:
            cnt += DFS(y+i, x, idx+1)
        if 0 <= x+i < M:
            cnt += DFS(y, x+i, idx+1)
    visited[y][x][idx] = cnt
    return cnt


res = 0
for n in range(N):
    for m in range(M):
        if maps[n][m] == word[0]:
            res += DFS(n, m, 0)

print(res)
