C = int(input())


def findZero(lo, hi, diff, N):
    lo_sol = 0
    for j in range(N+1):
        lo_sol += diff[j] * (lo ** (N-j))

    hi_sol = 0
    for j in range(N+1):
        hi_sol += diff[j] * (hi ** (N-j))

    if hi_sol < lo_sol:
        hi, lo = lo, hi

    half = (hi+lo) / 2

    for i in range(100):
        sol = 0
        for j in range(N+1):
            sol += diff[j] * (half ** (N-j))
        if -1 * 10**(-11) <= round(sol, 10) <= 10**(-11):
            return half

        if sol > 0:
            hi = half
            half = (hi+lo) / 2
        else:
            lo = half
            half = (hi+lo) / 2


def DFS(N, diff):
    if N == 1:
        return [-10, (-1*diff[1]) / diff[0], 10]

    n = N-1
    n_diff = []
    for i in range(N, 0, -1):
        n_diff.append(i * diff[N-i])

    section = DFS(n, n_diff)
    res = [-10]

    for i in range(N):
        lo = section[i]
        hi = section[i+1]
        res.append(findZero(lo, hi, diff, N))
    res.append(10)
    return res


for _ in range(C):
    N = int(input())
    origin = list(map(float, input().split()))
    res = DFS(N, origin)

    print(" ".join(map(str, res[1:-1])))
