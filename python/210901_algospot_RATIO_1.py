T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Z = int(M * 100 / N)
    Max = 2000000000

    if int((M+Max) * 100 / (N+Max)) == Z:
        print(-1)
    else:
        hi = Max
        lo = 0

        while lo + 1 < hi:
            half = (hi+lo) // 2
            Z_ = int((M+half) * 100 / (N+half))
            if Z == Z_:
                lo = half
            else:
                hi = half
        print(hi)
