def perm(n, k): # 재귀 이용
    if n == k:
        print(a)

    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

a = [1, 2, 3]

perm(3, 0)