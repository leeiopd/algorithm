N, M = map(int, input().split())
nums = list(map(int, input().split()))
s, e = 0, 1
tmp = nums[0]
res = 0

while s < e:
    if tmp == M:
        res += 1
        tmp -= nums[s]
        s += 1
        continue

    if e == N and tmp < M:
        break

    if tmp < M:
        tmp += nums[e]
        e += 1
        continue

    if tmp > M:
        tmp -= nums[s]
        s += 1
        continue


print(res)
