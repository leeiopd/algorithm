# 비트마스크 _ 에라토스테네스의 체

# 정수배열을 사용한 에라토스테네스의 체는
# 32비트 정수가 표현 할 수 있는 범위내의 모든 수에 대해 수행 할 시
# 상당히 많은 메모리를 차지하게 된다.

# C++ 의 경우 boolean 값 배열을 이용하지만 32비트 정수가 표혈 할 수 있는 범위 내의 모든 수를 수행 할 시
# 4기가바이트의 메모리가 필요하다.

# 짝수를 제외하여 2기가바이트로 줄일 수도 있지만,
# 비트마스크를 사용하면 메모리 사용량을 1/8 로 줄일 수 있다.


# 1.
SIZE = 2 ** 16 + 1  # Size is too big... Isn't it?

# 2.
sieve = [255 for _ in range(SIZE // 8 + 1)]


# 3.
def set_composite(n):
    sieve[n >> 3] &= ~(1 << (n & 7))


# 4.
set_composite(0)
set_composite(1)


# 5.
def is_prime(n):
    return True if sieve[n >> 3] & (1 << (n & 7)) else False


# 6.
for i in range(2, int(SIZE ** (1/2))+1):
    if is_prime(i):
        for j in range(i*i, SIZE+1, i):
            set_composite(j)
