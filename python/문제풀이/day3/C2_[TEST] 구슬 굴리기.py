'''
맵안에서 구슬을 주어진 방향대로 굴려서 지나간 자리의 칸수를 세는 문제이다
구슬은 굴러가다가 벽이나 기둥에 막힐 때마다 주어진 방향 순서대로 방향을 전환하여 굴러간다.
맵 안에 기둥은 1, 구슬은 2이며 0은 길이다.
구슬이 지나간 자리의 칸수를 출력한다.
뱡향은 1은 위, 2는 아래, 3은 왼쪽, 4는 오른쪽방향을 의미한다.
예로 다음과 같은 맵에서 2 3 1 4 1 3 방향이 주어질때 순서대로 구슬이 굴러간 자리의 칸수는 모두 13칸이다
단 한번 지나간 길을 다시 지나가는 경우는 중복하여 카운트하지 않는다. 구슬이 있는 시작자리부터 1개로 카운트에 포함한다

맵의 가로, 세로크기가 주어진다.(맵의 최대크기는 10*10)
맵의 정보가 주어진다.
방향을 전환할 순서 N개가 주어진다.
N개의 방향정보가 주어진다(N은 최대 12개)

지나간 자리의 개수를 출력한다.
'''
import sys

sys.stdin = open("C2_input.txt")

X_long, Y_long = map(int, input().split())

maps = []
for y in range(Y_long):
    maps.append(list(map(int, list(input()))))

N = int(input())

nums = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]  # 1은 위, 2는 아래, 3은 왼쪽, 4는 오른쪽방향
dy = [0, -1, 1, 0, 0]

for i in range(Y_long):
    for j in range(X_long):
        if maps[i][j] == 2:
            x = j
            y = i
cnt = 1
maps[y][x] = 3

for n in nums:
    X = x + dx[n]
    Y = y + dy[n]

    if n == 1 and Y > -1:
        for i in range(Y_long):
            y += dy[n]
            if y < 0 or maps[y][x] == 1:
                y -= dy[n]
                break
            if maps[y][x] != 3:
                cnt += 1
                maps[y][x] = 3

    if n == 2 and Y < N:
        for i in range(Y_long):
            y += dy[n]
            if y > Y_long-1 or maps[y][x] == 1:
                y -= dy[n]
                break
            if maps[y][x] != 3:
                cnt += 1
                maps[y][x] = 3

    if n == 3 and X > -1:
        for i in range(X_long):
            x += dx[n]
            if x < 0 or maps[y][x] == 1:
                x -= dx[n]
                break
            if maps[y][x] != 3:
                cnt += 1
                maps[y][x] = 3

    if n == 4 and X < N:
        for i in range(X_long):
            x += dx[n]
            if x > X_long-1 or maps[y][x] == 1:
                x -= dx[n]
                break
            if maps[y][x] != 3:
                cnt += 1
                maps[y][x] = 3

print(cnt)