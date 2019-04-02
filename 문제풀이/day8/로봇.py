import sys
sys.stdin  = open("로봇.txt")
'''
많은 공장에서 로봇이 이용되고 있다.
우리 공장의 로봇은 바라보는 방향으로 궤도를 따라 움직이며 움직이는 방향은 동 서 남 북 가운데 하나이다.
로봇의 이동을 제어하는 명령어는 다음과 같이 두 가지이다.
*명령 1. Go k
- k 는 1 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k 칸만큼 움직인다.
*명령 2. Turn dir 
- dir 은 left 또는 right 이며 각각 왼쪽 또는 오른쪽으로 90° 회전한다.
공장 내 궤도가 설치되어 있는 상태가 아래와 같이 0과 1로 이루어진 직사각형 모양으로 로봇에게 입력된다.
0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점이고 1은 궤도가 없어 로봇이 갈 수 없는 지점이다.
로봇이 (4, 2) 지점에서 남쪽을 향하고 있을 때 이 로봇을 (2, 4) 지점에서 동쪽으로 향하도록 이동시키는 것은 아래와 같이 9번의 명령으로 가능하다.

로봇의 현재 위치와 바라보는 방향이 주어졌을 때 로봇을 원하는 위치로 이동시키고 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램을 작성하시오.

첫째 줄에 공장 내 궤도 설치 상태를 나타내는 직사각형의 세로 길이 M과 가로 길이 N이 빈칸을 사이에 두고 주어진다.
이 때 M과 N은 둘 다 100이하의 자연수이다.
이어 M줄에 걸쳐 한 줄에 N개씩 각 지점의 궤도 설치 상태를 나타내는 숫자 0 또는 1이 빈칸을 사이에 두고 주어진다.
다음 줄에는 로봇의 출발 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다.
마지막 줄에는 로봇의 도착 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어진다.
방향은 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4로 주어진다. 출발지점에서 도착지점까지는 항상 이동이 가능하다.

첫째 줄에 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수를 출력한다.
'''
M, N = map(int, input().split())

maps = [[0 for x in range(N+1)]]

for m in range(M):
    maps.append([0] + list(map(int, input().split())))

rec = [[99 for x in range(N+1)]for y in range(M+1)]


start_x, start_y, start_d = map(int, input().split())
end_x, end_y, end_d = map(int, input().split())

queue = [[start_x, start_y, start_d]]
rec[start_x][start_y] = 0
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]

while queue:

    x, y, d = queue.pop(0)
    if x == end_x and y == end_y:
        if d != end_d:
            if d + 1 == end_d:
                d += 1
            elif  d - 1 == end_d:
                d -= 1
        maps[end_y][end_x] = d
        break


    for i in range(1, 5):
        X = x + dx[i]
        Y = y + dy[i]
        if X > -1 and X < N and Y > -1 and Y < M and maps[Y][X] == 0:
            k = 0
            if i != d:
                if d + 1 == i:
                    d += 1
                    k += 1
                elif d - 1 == i:
                    d -= 1
                    k += 1
                else:
                    d = (d + 2)%4
                    k += 2
            rec[Y][X] = rec[y][x] + 1 + k
            queue.append([X, Y, d])



print(maps[end_y][end_x])