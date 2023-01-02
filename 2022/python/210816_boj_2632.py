import sys

input = sys.stdin.readline

BUY = int(input())

M, N = map(int, input().split())

A = []
for _ in range(M):
    A.append(int(input()))

B = []
for _ in range(N):
    B.append(int(input()))

A_dic = {}
A_dic[0] = 1
A_dic[sum(A)] = 1
for l in range(1, M):
    s = 0
    e = s+l
    tmp = sum(A[s:e])
    while s < M:
        if tmp not in A_dic:
            A_dic[tmp] = 1
        else:
            A_dic[tmp] += 1

        tmp -= A[s]
        s += 1

        tmp += A[e]
        e += 1
        if e >= M:
            e %= M

res = 0
if BUY in A_dic:
    res += A_dic[BUY]
if BUY - sum(B) in A_dic:
    res += A_dic[BUY-sum(B)]

for l in range(1, N):
    s = 0
    e = s+l
    tmp = sum(B[s:e])
    while s < N:
        if BUY - tmp in A_dic:
            res += A_dic[BUY-tmp]

        tmp -= B[s]
        s += 1

        tmp += B[e]
        e += 1
        if e >= N:
            e %= N

print(res)
