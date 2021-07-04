N = int(input())

times = []

for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: (x[1], x[0]))
res = 1
end = times[0][1]

for s, e in times[1:]:
    if s >= end:
        res += 1
        end = e

print(res)
