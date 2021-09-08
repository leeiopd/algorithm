# 간단한 소인수 분해 알고리즘
# 시간복잡도 O( N ** 0.5 )
def factorSimple(N):
    ret = []
    sqrtn = int(N ** 0.5)

    # 소수가 아닌 [2, N**0.5] 범위의 모든 정수로 시도
    for div in range(2, sqrtn+1):
        while(N % div == 0):
            N //= div
            ret.append(div)

    if (N > 1):
        ret.append(N)

    return ret


print(factorSimple(28))
