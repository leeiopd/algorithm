T = int(input())


def checkC(N, M, P, C):
    for _ in range(M):
        N += (N * P / 12 / 100)
        N -= C
    return N


for _ in range(T):
    N, M, P = input().split()
    N = float(N)
    M = int(M)
    P = float(P)

    # 가장 큰 금액 - 원금 + 이자 : 할부금은 한번도 값지 않은 상황
    hi = N + (N * P / 12 / 100)
    lo = 0
    C = (hi+lo) / 2

    for _ in range(100):
        if checkC(N, M, P, C) < 0:
            hi = C
            C = (hi+lo) / 2
        else:
            lo = C
            C = (hi+lo) / 2
    print(C)
