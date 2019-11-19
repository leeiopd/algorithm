def myprint(q):
    while q != 0:
        q -= 1
        print(" %d " % (T[q]), end= "")
    print()

def H(n, r, q):
    if r == 0:
        myprint(q)  # 하고싶은 동작을 하는 부분 여기서는 출력

    elif n == 0:
        return

    else:
        T[r-1] = A[n-1]
        H(n, r-1, q)   # 선택 하는 경우
        H(n-1, r, q)   # 선택하지 않는 경우

A = [1, 2, 3 ,4]
T = [0] * 3

H(4, 3, 3)
