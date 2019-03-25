'''
첫 줄에 미로의 크기 X, Y(1≤X, Y≤100)가 주어진다.
둘째 줄에 출발점 x, y 좌표와 도착점 x, y 좌표가 공백으로 구분하여 주어진다.
셋째 줄부터 미로의 정보가 길은 0, 벽은 1로 공백이 없이 들어온다.
주의 사항으로, 좌표는 좌측상단이 가장 작은 위치이며 이 위치의 좌표는 (1,1)이다.


'''
import sys

sys.stdin = open("6_input.txt")


X, Y = map(int, input().split())

start_x, start_y, end_x, end_y = map(int, input().split())

maps = [[1 for x in range(X+2)]]

for y in range(Y):
    y_line = [1] + list(map(int, input())) + [1]
    maps.append(y_line)

maps.append([1for x in range(X+2)])

cnt = 0
queue = [[start_x, start_y, cnt]]
maps[start_y][start_x] = '*'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y, cnt = queue.pop(0)
    cnt += 1
    if x == end_x and y == end_y:
        break
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if maps[next_y][next_x] == 0:
            maps[next_y][next_x] = cnt
            queue.append([next_x, next_y, cnt])



print(maps[end_y][end_x])