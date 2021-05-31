N, B = input().split()

N = N[::-1]
B = int(B)

nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = 0

for i in range(len(N)):
    res += nums.index(N[i]) * (B ** i)

print(res)
