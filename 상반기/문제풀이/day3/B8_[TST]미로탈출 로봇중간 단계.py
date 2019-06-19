'''
지헌이는 미로를 탈출하는 로봇을 만들고 있다. 그런데 벽이나 장애물을 만났을 때만 주어진 방향 순서대로 바꾸어 갈 수 있는지를 테스트 하려고 한다.

< 처리조건 >
1. 출발은 항상 왼쪽 위에서 시작한다.
2. 벽이나 장애물을 만났을 때만 방향을 바꿀 수 있다. (벽은 맵의 바깥을 말함)
3. 방향을 바꿀 때는 주어진 순서대로 바꾼다. (4방향 모두 이동시키면 다시 처음 방향부터 반복 이동시킴)
4. 한번 지나간 길은 다시 지나갈 수 없다. 즉 로봇 동작은 멈춘다
5. 맵의 1칸 이동을 이동거리 1로 한다.

5x5맵의 정보가 주어지고 방향의 순서가 아래, 오른쪽, 위. 왼쪽 일 때 다음과 같이 움직인다.



미로의 맵과 방향의 순서가 주어질 때 최대로 이동할 수 있는 이동 거리를 구하는 프로그램을 작성하시오.


첫 줄에 맵의 가로, 세로 크기인 N(3≤N≤10)이 들어온다.
그 다음 줄부터 N개의 줄에 각각 N개씩 0과 1이 공백 없이 들어온다. (0: 길, 1: 장애물)
마지막 줄에 방향을 바꾸는 순서 정보 4개가 들어온다. 방향을 바꾸는 순서 정보는 번호로 주어지며, 1은 아래, 2는 왼쪽, 3은 위, 4는 오른쪽을 의미한다.

출발위치에서 출발하여 방향 순서대로 이동할 경우 최대로 이동할 수 있는 거리를 출력한다.
'''

import sys

sys.stdin = open("B8_input.txt")

N = int(input())

maps = []

for n in range(N):
    maps.append(list(map(int, list(input()))))

direction = list(map(int, input().split()))


dx = [0, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]
cnt = 0
x = 0
y = 0
k = 0
maps[x][y] = 9
flag = 1
while flag != 0:
    k = k%4
    i = direction[k]

    X = x + dx[i]
    Y = y + dy[i]

    if i == 1:
        if Y < N and maps[Y][X] == 9:
            break
        while True:
            y += dy[i]
            if y < N and maps[y][x] == 9:
                flag = 0
                break

            if y > N-1 or maps[y][x] == 1:
                y -= dy[i]
                break
            cnt += 1
            maps[y][x] = 9

    if i == 4:
        if X < N and maps[Y][X] == 9:
            break
        while True:
            x += dx[i]
            if x < N and maps[y][x] == 9:
                flag = 0
                break
            if x > N-1 or maps[y][x] == 1:
                x -= dx[i]
                break
            cnt += 1
            maps[y][x] = 9

    if i == 3:
        if Y > -1 and maps[Y][X] == 9:
            break
        while True:
            y += dy[i]
            if y > -1 and maps[y][x] == 9:
                flag = 0
                break
            if y < 0 or maps[y][x] == 1:
                y -= dy[i]
                break
            cnt += 1
            maps[y][x] = 9

    if i == 2:
        if X > -1 and maps[Y][X] == 9:
            break
        while True:
            x += dx[i]
            if x > -1  and maps[y][x] == 9:
                flag = 0
                break
            if x < 0  or maps[y][x] == 1:
                x -= dx[i]
                break
            cnt += 1
            maps[y][x] = 9
    k += 1

print(cnt)