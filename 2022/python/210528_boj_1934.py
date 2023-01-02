import sys
import math
N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(math.lcm(A, B))
