N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = A+B
res.sort()

print(" ".join(map(str, res)))
