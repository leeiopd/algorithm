# 선택정렬 : 지정된 위치에 최소값을 찾아 가져오는 방법
# ex) [2, 6, 1, 4]
#       1. [1, 6, 2, 4]
#       2. [1, 2, 6, 4]
#       3, [1, 2, 4, 6]


def selectioinsort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
            temp = A[min]
            A[min] = A[i]
            A[i] = temp


def recselectionsort(ary, s, e):  # 재귀로 구현
    mini = s

    if s == e:
        return

    for j in range(s+1, e):
        if ary[j] < ary[mini]:
            mini = j

    ary[s], ary[mini] = ary[mini], ary[s]

    recselectionsort(ary, s+1, e)
