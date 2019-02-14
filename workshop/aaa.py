'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고
(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로
이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.

아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라
(‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
'''

import sys

sys.stdin = open("07_input.txt")

T = 10


def right(maps):
    global x, y
    if x < 99 and maps[y][x + 1] == '1':
        x += 1
        return right(maps)
    else:
        return x


def left(maps):
    global x, y
    if x > 0 and maps[y][x - 1] == '1':
        x -= 1
        return left(maps)
    else:
        return x


for t in range(1, T + 1):
    case = int(input())
    ladder = []
    for i in range(100):
        line = list(input().split())
        ladder.append(line)

    result = [0] * 100
    lenth_min = 1000

    for i in range(100):
        y = 0
        x = i
        start = i
        if ladder[0][x] == '1':
            lenth = 0

            while y < 99:
                if x < 99 and ladder[y][x + 1] == '1':
                    x = right(ladder)
                    lenth += 1
                elif x > 0 and ladder[y][x - 1] == '1':
                    x = left(ladder)
                    lenth += 1
                y += 1
                lenth += 1
            result[i] = lenth
            if lenth < lenth_min and ladder[y][x] == '1':
                lenth_min = lenth
                result_index = start
    print(f'#{case} {result_index}')
    print(f'{result}')