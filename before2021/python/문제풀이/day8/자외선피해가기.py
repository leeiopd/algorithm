import sys
sys.stdin  = open("자외선피해가기.txt")
'''
영희는 자외선이 피부에 좋지 않기 때문에 이동 시 자외선에 노출되는 것을 최소한으로 하고 싶어서 가는 길의 자외선 양을 모두 조사하였다.
값이 제 각각이어서 어떤 경로로 가야 좋을지 난감한 영희를 도와주자.
N*N 모양의 장소의 모든 길의 자외선 양이 주어지고 영희는 상하좌우 한 칸씩만 이동이 가능하다.
시작점(1,1)에서 도착점(N,N)까지 이동 시 자외선 합의 최소값을 찾아라.
예를 들어 3*3 장소의 자외선 양이 아래와 같다면 오른쪽처럼 이동하면 8만큼만 노출된다.

첫 줄에 N(2≤N≤100)이 들어온다.
그 다음 줄부터 N개의 줄에 각각 N개씩 M(0≤M≤9)이 공백 없이 들어온다.

출발점에서 도착점까지 자외선 합의 최소값을 출력한다.
'''
N = int(input())

maps = []

for n in range(N):
    maps.append(list(map(int, input())))

rec = [[999999 for x in range(N)]for y in range(N)]
rec[0][0] = maps[0][0]

queue = []
route = []
queue.append([0, 0])
result = 99999999999999999999
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while queue:

    x, y = queue.pop(0)

    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X > -1 and X < N and Y > -1 and Y < N:
            if rec[y][x] + maps[Y][X] < rec[Y][X]:
                rec[Y][X] = rec[y][x] + maps[Y][X]
                queue.append([X, Y])

print(rec[N-1][N-1])