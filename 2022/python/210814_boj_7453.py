
N = int(input())

A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

add_A_B = {}
for a in A:
    for b in B:
        if a+b not in add_A_B:
            add_A_B[a+b] = 1
        else:
            add_A_B[a+b] += 1

res = 0

for c in C:
    for d in D:
        if -(c+d) in add_A_B:
            res += add_A_B[-(c+d)]

print(res)
