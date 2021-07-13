import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for _ in range(N):
    nums.append(list(map(int, list(input()[:-1]))))


# 123
# 123
# 123
res_1 = 0
for s in range(1, M-1):
    for e in range(M-1, s, -1):
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        for n in range(N):
            tmp1 += sum(nums[n][:s])
            tmp2 += sum(nums[n][s:e])
            tmp3 += sum(nums[n][e:])
        res_1 = max(res_1, tmp1*tmp2*tmp3)

# 111
# 222
# 333
res_2 = 0
for s in range(1, N-1):
    for e in range(N-1, s, -1):
        tmp1 = 0
        for i in range(s):
            tmp1 += sum(nums[i])

        tmp2 = 0
        for i in range(s, e):
            tmp2 += sum(nums[i])

        tmp3 = 0
        for i in range(e, N):
            tmp3 += sum(nums[i])
        res_2 = max(res_2, tmp1*tmp2*tmp3)


# 122
# 133
# 133
res_3 = 0
for m in range(1, M):
    tmp1 = 0
    for n in range(N):
        tmp1 += sum(nums[n][:m])

    for n in range(1, N):
        tmp2 = 0
        tmp3 = 0
        for i in range(n):
            tmp2 += sum(nums[i][m:])
        for i in range(n, N):
            tmp3 += sum(nums[i][m:])
        res_3 = max(res_3, tmp1 * tmp2 * tmp3)

# 113
# 223
# 223
res_4 = 0
for m in range(M-1, 0, -1):
    tmp1 = 0
    for n in range(N):
        tmp1 += sum(nums[n][m:])

    for n in range(1, N):
        tmp2 = 0
        tmp3 = 0
        for i in range(n):
            tmp2 += sum(nums[i][:m])
        for i in range(n, N):
            tmp3 += sum(nums[i][:m])
        res_4 = max(res_4, tmp1 * tmp2 * tmp3)

# 111
# 223
# 223
res_5 = 0
for n in range(1, N):
    tmp1 = 0
    for i in range(n):
        tmp1 += sum(nums[i])

    tmp2 = 0
    tmp3 = 0
    for j in range(1, M):
        tmp2 = 0
        tmp3 = 0
        for i in range(n, N):
            tmp2 += sum(nums[i][:j])
            tmp3 += sum(nums[i][j:])
        res_5 = max(res_5, tmp1 * tmp2 * tmp3)

# 112
# 112
# 333
res_6 = 0
for n in range(1, N):
    for j in range(1, M):
        tmp2 = 0
        tmp3 = 0
        for i in range(n):
            tmp2 += sum(nums[i][:j])
            tmp3 += sum(nums[i][j:])
        tmp1 = 0
        for i in range(n, N):
            tmp1 += sum(nums[i])
        res_6 = max(res_6, tmp1 * tmp2 * tmp3)

print(max(res_1, res_2, res_3, res_4, res_5, res_6))
