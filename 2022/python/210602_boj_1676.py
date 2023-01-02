N = int(input())
res = 1
for i in range(2, N+1):
    res *= i

res = str(res)[::-1]

for i in range(len(res)):
    if res[i] != '0':
        print(i)
        break
