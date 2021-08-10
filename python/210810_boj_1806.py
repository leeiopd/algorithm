N, S = map(int, input().split())

nums = list(map(int, input().split()))

s, e = 0, 1
add = nums[0]
res = N+1

while True:
    if e == N and add < S:
        break

    if add >= S:
        res = min(res, e-s)
        add -= nums[s]
        s += 1

    elif add < S:
        add += nums[e]
        e += 1

    else:
        add -= nums[s]
        s += 1

print(0 if res == N+1 else res)
