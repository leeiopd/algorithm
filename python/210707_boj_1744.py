import sys
input = sys.stdin.readline

N = int(input())

nums_p = []
nums_m = []

for _ in range(N):
    tmp = int(input())
    if tmp > 0:
        nums_p.append(tmp)
    else:
        nums_m.append(tmp)

nums_p.sort(reverse=True)
res = 0
for i in range(len(nums_p)//2):
    if nums_p[(i*2)+1] == 1:
        res += nums_p[i*2]
        res += nums_p[(i*2)+1]
    else:
        res += nums_p[i*2] * nums_p[(i*2)+1]
if len(nums_p) % 2:
    res += nums_p[-1]

nums_m.sort()
for i in range(len(nums_m)//2):
    res += nums_m[i*2] * nums_m[(i*2)+1]
if len(nums_m) % 2:
    res += nums_m[-1]

print(res)
