import math

A, B = map(int, input().split())

C = math.gcd(A, B)

for _ in range(C):
    print("1", end="")
