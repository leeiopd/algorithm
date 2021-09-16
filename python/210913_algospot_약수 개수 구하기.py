# 1천만 이하의 모든 수의 약수의 개수를 계산하는 알고리즘

Max = 10000000

# 가장 작은 소인수
minFactor = [x for x in range(Max+1)]
minFactor[0] = 0
minFactor[1] = 1

sqrtn = int(Max ** 0.5)

for i in range(2, sqrtn+1):
    if minFactor[i] == i:
        for j in range(i*i, Max+1, i):
            if minFactor[j] == j:
                minFactor[j] = i


# minFactorPower[i] = i 의 소인수 분해에는 minFactor[i]의 몇승이 포함되는지
minFactorPower = [0] * (Max + 1)

# factors[i] = i 가 가진 약수의 개수
factors = [0] * (Max + 1)


def getFactorsSmart():
    global Max, minFactor, minFactorPower, factors

    # 1의 약수는 1개
    factors[1] = 1

    for i in range(2, Max+1):
        # 소수인 경우
        if minFactor[i] == i:
            # i ** 1 승
            minFactorPower[i] = 1
            # 소수 [1, i] -> 2개
            factors[i] = 2
        else:
            p = minFactor[i]

            m = int(i / p)

            if p != minFactor[m]:
                minFactorPower[i] = 1
            else:
                minFactorPower[i] = minFactorPower[m] + 1

            a = minFactorPower[i]
            factors[i] = int((factors[m]/a) * (a+1))


getFactorsSmart()
