# O(N ** 0.5) 시간에 동작하는 소수 판별 알고리즘

def isPrime(N):
    if (N <= 1):
        return False
    if (N <= 2):
        return True

    # 2의 배수 (짝수) 제외
    if not (N % 2):
        return False

    # 합성수 N = p * q 일 때, p <= (N ** 0.5) && q >= (N ** 0.5) 이므로,
    # ( N ** 0.5 ) 까지 순회하는 것으로 합성수 판별이 가능하다.
    sqrtn = int(N ** 0.5)

    # 3이상의 홀수로 나누어 판별, 짝수를 제외한 경우에 대해서 판별
    for div in range(3, sqrtn+1, 2):
        if not (N % div):
            return False
    return True


print(isPrime(14))
