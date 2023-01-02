N = int(input())

primes = [1] * (N+1)
primes[0] = 0

nums = []

for i in range(2, N+1):
    if not primes[i]:
        continue
    nums.append(i)
    for j in range(i + i, N+1, i):
        primes[j] = 0

s, e = 0, 1
if nums:
    add = nums[s]

L = len(nums)

res = 0


while L:
    if e == L and add < N:
        break

    if add == N:
        res += 1
        add -= nums[s]
        s += 1
    elif add > N:
        add -= nums[s]
        s += 1
    else:
        add += nums[e]
        e += 1

print(res)
