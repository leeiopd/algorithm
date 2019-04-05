import sys
sys.stdin = open("미로탈출.txt")
'''
로봇이 벽(1)으로 막힌 공간안에서 시작점(3)에서 시작하여 탈출점(4)으로 나가는 최단거리를 구하는 문제이다. 
[조건]
1] 로봇은 상하좌우로 이동이 가능하며 0은 갈수 있는 길이다.
2] 2는 막혀있는 길이지만 폭탄으로 허물 수 있는 벽이다. 
3] 폭탄은 3개를 지니고 있다.
4] 외벽 가장자리에는 모두 벽(1)으로 둘러져 있다 . 1인 벽은 폭탄으로 허물수 없는 막힌 벽이다
5] 시작점(3)에서 시작하여 탈출점(4)으로 가는데 폭탄 3개 이하로 터트려 가는 최단 경로를 구한다.

첫줄에 맵의 세로크기R , 가로크기 C가 주어진다. 맵크기는 최대 30*30이다. 
둘째줄에 맵의 정보가 주어진다. 
맵의 각 점들은 0, 1, 2, 3, 4의 값으로 표시된다. 
0은 갈수 있는곳, 1은 벽으로 막힌곳, 2는 폭탄으로 허물수 있는 벽, 3은 시작점, 4는 탈출점이다.

3(시작점)에서 시작하여 4(탈출점)로 가는데 폭탄은 3개이하로 터트려 가는 최단 경로를 구한다. 
4(탈출점)에 도달할수 없는 상황이면 -1을 인쇄한다.'''

N, M = map(int, input().split())

maps = []
for n in range(N):
    maps.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        if maps[y][x] == 3:
            start_x = x
            start_y = y
        if maps[y][x] == 4:
            end_x = x
            end_y = y

rec = [[0 for x in range(M)] for y in range(N)]

cnt = 1
queue = [[start_x, start_y, cnt]]
rec[start_y][start_x] = 3
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = -1
visited = []
while queue:

    x, y, cnt = queue.pop(0)
    if [x, y] in visited:
        continue
    visited.append([x, y])

    if x == end_x and y == end_y:
        result = cnt
        break

    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if Y < N-1 and Y > 0 and X < N-1 and X > 0 and maps[Y][X] != 1:
                if maps[Y][X] == 2:
                    if rec[Y][X] < rec[y][x] - 1 and rec[y][x] > 0:
                        rec[Y][X] = rec[y][x] - 1
                        queue.append([X, Y, cnt+1])
                else:
                    rec[Y][X] = rec[y][x]
                    queue.append([X, Y, cnt+1])

print(result-1)