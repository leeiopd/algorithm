T = int(input())

N = int(input())
n_list = list(map(int, input().split()))

check = {}

for i in range(N):
    tmp = n_list[i]
    if tmp not in check:
        check[tmp] = 1
    else:
        check[tmp] += 1
    for j in range(i+1, N):
        tmp += n_list[j]
        if tmp not in check:
            check[tmp] = 1
        else:
            check[tmp] += 1


M = int(input())
m_list = list(map(int, input().split()))

res = 0

for i in range(M):
    tmp = m_list[i]
    if T-tmp in check:
        res += check[T-tmp]
    for j in range(i+1, M):
        tmp += m_list[j]

        if T-tmp in check:
            res += check[T-tmp]

print(res)
