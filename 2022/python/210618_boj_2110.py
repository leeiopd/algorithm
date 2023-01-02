N, C = map(int, input().split())

house = []

for _ in range(N):
    house.append(int(input()))

house.sort()
end = house[-1] - house[0]
start = 1
res = 0
while start <= end:
    mid = (start+end)//2

    cnt = 1

    for i in range(1, N):
        if house[i] - house[i-1] >= mid:
            cnt += 1

    if cnt < C:
        end = mid - 1
    else:
        start = mid + 1
        res = mid

print(res)
