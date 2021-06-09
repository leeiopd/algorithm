T = int(input())

for _ in range(T):
    N = int(input())
    picks = [0] + list(map(int, input().split()))

    visited = [0] * (N+1)
    res = 0

    for i in range(1, N+1):
        if visited[i]:
            continue
        f = i
        loop = [f]
        visited[f] = 1
        while True:
            t = picks[f]
            if visited[t]:
                break
            f = t
            loop.append(f)
            visited[f] = 1

        if loop and t in loop:
            res += len(loop[loop.index(t):])
    print(N - res)
