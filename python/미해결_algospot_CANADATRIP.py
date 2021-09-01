import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    road = [0] * 8030001

    for i in range(N):
        L, M, G = map(int, input().split())

        road[L] += 1
        for _ in range(M//G):
            L -= G
            road[L] += 1

    hi = 8030001
    lo = 0

    while True:
        half = (hi+lo) // 2
        S = sum(road[:half])
        if S == K:
            half -= 1
            while road[half] == 0:
                half -= 1
            print(half)
            break

        if S > K:
            hi = half
        else:
            lo = half


# L : 시작점으로부터 도시까지 거리
# M : 표지판이 시작하는 지점, 도시에서부터 떨어진 거리
# G : 표지판 간격

# K 번째로 만나는 표지판의 위치
