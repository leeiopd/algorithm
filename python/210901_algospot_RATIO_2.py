T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Max = 2000000000

    if int((M+Max) * 100 / (N+Max)) == int(M*100/N):
        print(-1)
    else:
        res = (N * N) / (99 * N - 100 * M)

        if res % 1:
            print(int(res)+1)
        else:
            print(int(res))

# 승룰 계산이 소숫점 이하 버림이 된는것이 문제
