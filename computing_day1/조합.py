def myprint(q):
    while q != 0:
        q -= 1
        print(" %d " % (T[q]), end= "")
    print()

def comb(n, r, q):
    if r == 0:
        myprint(q)  # 하고싶은 동작을 하는 부분 여기서는 출력

    elif n < r:
        return

    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

A = [1, 2, 3 ,4]
T = [0] * 3

comb(4, 3, 3)

# 조합 구하기