answer = []

oneBlock_dy = [1, -1, 0, 0]
oneBlock_dx = [0, 0, 1, -1]


diagonal_dy = [1, 1, -1, -1]
diagonal_dx = [1, -1, 1, -1]


def check_oneBlock(place, y, x):
    for i in range(4):
        if place[y][x] == 'P':
            Y = y + oneBlock_dy[i]
            X = x + oneBlock_dx[i]
            if 0 <= Y < 5 and 0 <= X < 5 and place[Y][X] == 'P':
                return False
    return True


def check_twoBlock(place, y, x):
    for i in range(4):
        if place[y][x] == 'P':
            Y = y + (oneBlock_dy[i] * 2)
            X = x + (oneBlock_dx[i] * 2)
            if 0 <= Y < 5 and 0 <= X < 5 and place[Y][X] == 'P':
                if place[y + oneBlock_dy[i]][x + oneBlock_dx[i]] != 'X':
                    return False
    return True


def check_diagonal(place, y, x):
    for i in range(4):
        if place[y][x] == 'P':
            Y = y + diagonal_dy[i]
            X = x + diagonal_dx[i]
            if 0 <= Y < 5 and 0 <= X < 5 and place[Y][X] == 'P':
                if place[y][x+diagonal_dx[i]] != 'X' or place[y+diagonal_dy[i]][x] != 'X':
                    return False
    return True


def checkPlace(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == 'P':
                if not check_oneBlock(place, y, x):
                    answer.append(0)
                    return

                if not check_twoBlock(place, y, x):
                    answer.append(0)
                    return

                if not check_diagonal(place, y, x):
                    answer.append(0)
                    return
    answer.append(1)
    return


def solution(places):
    for place in places:
        checkPlace(place)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
