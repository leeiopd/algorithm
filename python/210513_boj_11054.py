N = int(input())

nums = list(map(int, input().split()))

upDp = [1] * N
downDp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            upDp[i] = max(upDp[i], upDp[j]+1)

    for k in range(N-1, N-1-i, -1):
        if nums[N-1-i] > nums[k]:
            downDp[N-1-i] = max(downDp[N-1-i], downDp[k]+1)

result = [0] * N
for i in range(N):
    result[i] = upDp[i] + downDp[i]


print(downDp)
print(max(result))
            