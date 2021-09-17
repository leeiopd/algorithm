# 1천만 이하의 모든 수의 약수의 개수를 계산하는 알고리즘
# 에라토스테네스의 체를 사용하지 않고, brute force 로 해결


Max = 10000000

factors = [0] * (Max + 1)


def getFactorsBrute():
    global factors
    for i in range(1, Max+1):
        for j in range(i, Max+1, i):
            factors[j] += 1


getFactorsBrute()
print(factors[:10])
