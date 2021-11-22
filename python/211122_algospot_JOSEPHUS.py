C = int(input())

for _ in range(C):
    N, K = map(int, input().split())

    alive = [x+1 for x in range(N)]
    kill = 0
    while len(alive) > 2:
        del alive[kill]
        kill = (kill+K-1) % len(alive)

    print(*alive)  # print(" ".join(map(str, alive)))
