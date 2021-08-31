T = int(input())


def checkC(N, M, P, C):
    for _ in range(M):
        N *= 1 + (P / 12) / 100
        N -= C
    return N


for _ in range(T):
    N, M, P = input().split()
    N = float(N)
    M = int(M)
    P = float(P)

    hi = N * (1 + (P / 12) / 100)
    lo = 0
    C = (hi+lo) / 2

    for i in range(100):
        res = checkC(N, M, P, C)

        if checkC(N, M, P, C) <= 0:
            hi = C
            C = (hi+lo) / 2
        else:
            lo = C
            C = (hi+lo) / 2

    print(C)
