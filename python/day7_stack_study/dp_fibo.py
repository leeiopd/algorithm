# DP 적용 알고리즘
def fibo(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


print(fibo(10000000))