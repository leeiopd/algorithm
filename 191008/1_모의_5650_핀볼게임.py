import sys
sys.stdin = open('5650.txt')

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def Game(start_x, start_y, i):
    global result
    score = 0
    x = start_x
    y = start_y
    while True:
        X = x + dx[i]
        Y = y + dy[i]

        if 0 <= X < N and 0 <= Y < N:
            # 블랙홀 조건
            if maps[Y][X] == -1:
                if result < score:
                    result = score
                return
            # 웜홀 조건
            if 6 <= maps[Y][X] <= 10:
                flag = 0
                for a in range(N):
                    if flag:
                        break
                    for b in range(N):
                        # 다른 웜홀로 이동
                        if maps[a][b] == maps[Y][X] and (a != Y or b != X):
                            X = b
                            Y = a
                            flag = 1
                            break
        # 시작위치 도달 종료 조건
        if X == start_x and Y == start_y:
            if result < score:
                result = score
            return

        # 이동 방향으로 구분
        # 좌
        if i == 0:
            if X < 0 or maps[Y][X] == 3 or maps[Y][X] == 4 or maps[Y][X] == 5:
                score += 1
                i = 1
            elif maps[Y][X] == 1:
                score += 1
                i = 2
            elif maps[Y][X] == 2:
                score += 1
                i = 3
        # 우
        elif i == 1:
            if X > N - 1 or maps[Y][X] == 1 or maps[Y][X] == 2 or maps[Y][X] == 5:
                score += 1
                i = 0
            elif maps[Y][X] == 3:
                score += 1
                i = 3
            elif maps[Y][X] == 4:
                score += 1
                i = 2
        # 상
        elif i == 2:
            if Y < 0 or maps[Y][X] == 1 or maps[Y][X] == 4 or maps[Y][X] == 5:
                score += 1
                i = 3
            elif maps[Y][X] == 2:
                score += 1
                i = 1
            elif maps[Y][X] == 3:
                score += 1
                i = 0
        # 하
        elif i == 3:
            if Y > N - 1 or maps[Y][X] == 2 or maps[Y][X] == 3 or maps[Y][X] == 5:
                score += 1
                i = 2
            elif maps[Y][X] == 1:
                score += 1
                i = 1
            elif maps[Y][X] == 4:
                score += 1
                i = 0
        x = X
        y = Y


for case in range(1, T + 1):
    N = int(input())
    maps = []
    for n in range(N):
        maps.append(list(map(int, input().split())))
    result = 0
    for y in range(N):
        for x in range(N):
            # 맵의 빈칸일때 (블록이나 웜홀 블랙홀이 없는 위치)
            if not maps[y][x]:
                # 네 방향으로 시작
                for i in range(4):
                    Game(x, y, i)
    print('#{} {}'.format(case, result))
