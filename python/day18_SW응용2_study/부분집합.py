count = 0
N = 3
A = [0 for x in range(N)]

data = [1, 2, 3]


result = []
def powerset(n, k):
    if n == k:
        r_list = [0] * N
        for i in range(N):
            r_list[i] = A[i]
        result.append(r_list)

    else:
        for i in range(2):
            A[k] = i
            powerset(n, k+1)

powerset(N, 0)
print(result)