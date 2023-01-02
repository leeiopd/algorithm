# 에라토스테네스의 체

def eratosthenes(N):
    nums = [1] * (N+1)

    nums[0] = 0
    nums[1] = 0

    sqrtn = int(N ** 0.5)

    for i in range(sqrtn+1):
        if nums[i]:
            # ( i+i = 2 * i ) 는 2의 배수를 지울 때, 3*i 는 3의 배수를 지울때 지워졌을 것이므로,
            # i * i 부터 탐색
            for j in range(i*i, N+1, i):
                nums[j] = 0
    return nums


print(eratosthenes(10))
