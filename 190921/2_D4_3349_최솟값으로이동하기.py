'''
한국의 모든 구획이 새롭게 재편성되었다.

정확히 말하면 W개의 남북방향 도로와 H개의 동서방향 도로가 모두 일정한 간격으로 늘어서서 교차하는 바둑판 모양으로 만들었다.

남북방향 도로는 가장 서쪽에 있는 것으로부터 시작해서 동쪽으로 가면서 차례대로 1, 2, …, W로 번호가 매겨져 있고,

동서방향 도로는 가장 남쪽에 있는 것으로부터 시작해서 북쪽으로 가면서 차례대로 1, 2, …, H로 번호가 매겨져 있다.

i번 남북방향 도로와 j번 동서방향 도로가 교차하는 지점을 (i, j)로 나타낸다.

이렇게 도로를 만들고 나면 아래와 같은 모양이 된다.

W = 4, H = 3인 예이다.



정부는 이런 식으로 도로를 만들면 중간에 사용하지 않는 공간이 너무 많은 것 같아서 북동방향으로 가는 도로도 만들었다.

즉 (i, j)와 (i - 1, j - 1)을 연결하는 도로이다.

이런 도로를 만든 다음에는 아래와 같아질 것이다.



준환이는 최근에 일이 많아서 N개의 교차로를 순서대로 이동해야 한다.

i번째로 이동하려는 지점은 (xi, yi)이다.

정부에서는 교차로에서 다른 교차로로 한번 이동할 때 1만큼의 비용을 내도록 정책을 세웠기 때문에 비용을 줄이기 위해 적절한 전략을 세워야 한다.

준환이는 (x1, y1)에서 시작하여 i가 증가하는 순서대로 (xi, yi)들을 차례대로 방문하고 (xN, yN)에 도착하기 위해 드는 비용의 최솟값이 무엇인지 궁금하다.

이를 구하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 정수 W, H, N(2 ≤ W, H ≤ 10,000, 1 ≤ N ≤ 1,000)이 공백으로 구분되어 주어진다.

다음 N개의 줄의 i번째 줄에는 두 정수 xi, yi (1 ≤ xi ≤ W, 1≤ yi ≤ H)가 공백으로 구분되어 주어진다.


[출력]

각 테스트 케이스마다 x1, y1 에서 시작하여 i가 증가하는 순서대로 (xi, yi) 들을 차례대로 방문하고 (xN, yN)에 도착하기 위해 드는 비용의 최솟값을 출력한다.
'''
import sys
sys.stdin = open('3349.txt')

# 비교적 간단한 로직이므로 DFS는 시간이 너무 오래 걸리게 된다
# 문제를 잘 읽고 더 나은 전략을 선택하자

T = int(input())

for case in range(1, T+1):
    W, H, N = map(int, input().split())
    nav = [0] * N
    for n in range(N):
        nav[n] = list(map(int, input().split()))
    startX,  startY = map(int, nav[0])
    result = 0
    for n in range(1, N):
        endX, endY = map(int, nav[n])
        if endX >= startX and endY >= startY:
            X = endX - startX
            Y = endY - startY
            if X > Y:
                result += X
            else:
                result += Y
        elif endX <= startX and endY <= startY:
            X = startX - endX
            Y = startY - endY
            if X > Y:
                result += X
            else:
                result += Y
        elif endX > startX and endY < startY:
            X = endX - startX
            Y = startY - endY
            result += (X + Y)
        elif endX < startX and endY > startY:
            X = startX - endX
            Y = endY - startY
            result += (X+Y)
        startX, startY = endX, endY
    print('#{} {}'.format(case, result))
