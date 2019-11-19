import sys
sys.stdin = open("미술관람대회.txt")
'''
해마다 열리는 꿀꿀이 올림피아드에는 여러 종목들이 있는데, 요즘에는 꿀꿀이들의 교양을 겨루는 ‘미술관람 대회’가 인기를 끌고 있다.
이 대회는 사회자가 빨강, 초록, 파랑으로 이루어진 N × N 픽셀의 그림을 보여주면 그 그림에 포함된 영역의 수를 빠르고 정확하게 맞추는 것이 목표이다.
동일한 색깔이 네 방향(상, 하, 좌, 우) 중 한 곳이라도 연결되어 있으면 하나의 영역으로 간주한다.
 
예를 들어, 아래 그림은 각각 2, 1, 1개의 빨간색, 초록색, 파란색 영역이 있어 총 4개의 영역이 있다.
한편, 꿀꿀이들의 절반 정도는 선천적인 유전자 때문에 적록색맹이라서 빨간색과 초록색을 구별하지 못한다.
따라서 사회자는 일반 대회와 적록색맹용 대회를 따로 만들어서 대회를 진행하려고 한다. 사회자를 도와 영역의 수를 구하는 프로그램을 작성하여라.

첫 번째 줄에는 그림의 크기 N이 주어진다. (1 ≤ N ≤ 60)
두 번째 줄부터 N개의 줄에는 각 픽셀의 색깔이 'R'(빨강), 'G'(초록), 'B'(파랑) 중 하나로 주어진다.

일반 꿀꿀이와 적록색맹 꿀꿀이가 보는 영역의 수를 출력한다.
'''
N = int(input())

maps = []
maps_pig = [[0 for x in range(N)]for y in range(N)]
for n in range(N):
    maps.append(list(input()))

for y in range(N):
    for x in range(N):
        if maps[y][x] == 'G':
            maps_pig[y][x] = 'R'
        else:
            maps_pig[y][x] = maps[y][x]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

color = 0
pig_color = 0

def check(x, y, color, maps):
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]

        if X > -1 and X < N and Y > -1 and Y < N and maps[Y][X] == color:
            maps[Y][X] = 0
            check(X, Y, color, maps)

for y in range(N):
    for x in range(N):
        if maps[y][x] != 0:
            color += 1
            check(x, y, maps[y][x], maps)
            maps[y][x] = 0
        if maps_pig[y][x] != 0:
            pig_color += 1
            check(x, y, maps_pig[y][x], maps_pig)

print(color, pig_color)
