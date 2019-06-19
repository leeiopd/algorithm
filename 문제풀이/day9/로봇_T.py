import sys
sys.stdin = open("로봇.txt")
M, N = map(int, input().split())
maps = [[0]*(N+1)]
for m in range(M):
    maps.append([0] + list(map(int, input().split())))

start_y, start_x, start_d = map(int, input().split())
end_y, end_x, end_d = map(int, input().split())

queue = [[start_x, start_y, start_d, 0]]

result = 0
check = [[[0 for x in range(N+1)] for y in range(M+1)] for d in range(5)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
turn = [(0, 0), [4, 3], [3, 4], [1, 2], [2, 1]]

while queue:

    x, y, d, cnt = queue.pop(0)

    if x == end_x and y == end_y and d == end_d:
        result = cnt
        break

    for i in range(1, 4):
        X = x + dx[d] * i
        Y = y + dy[d] * i
        if X < 0 or X >=N or Y < 0 or Y >=N:
            break
        if maps[Y][X]:
            break
        if check[d][Y][X]:
            continue
        queue.append([X, Y, d, cnt+1])
        check[d][Y][X] = 1

    for i in range(2):
        next_d = turn[d][i]
        if check[next_d][y][x]:
            continue
        queue.append([x, y, next_d, cnt+1])
        check[next_d][y][x] = 1


print(result)