digit = input()
digit = digit[::-1]

res = ""
tmp = 0
for i in range(len(digit)):
    if i == 0:
        tmp = int(digit[0])
        continue

    k = i % 3
    if digit[i] == '1':
        tmp += 2 ** k
    if k == 2:
        res += str(tmp)
        tmp = 0

res += str(tmp) if tmp else ""

print(res[::-1] if res else 0)
