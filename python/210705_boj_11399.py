N = int(input())

times = list(map(int, input().split()))
times.sort()
res = [0] * N
res[0] = times[0]

for i in range(1, N):
    res[i] = res[i-1] + times[i]

print(sum(res))
