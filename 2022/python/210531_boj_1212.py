eights = input()

res = ""

for i in range(len(eights)):
    n = int(eights[i])

    tmp = ""

    while n != 0:
        tmp += str(n % 2)
        n //= 2

    if i != 0:
        while len(tmp) < 3:
            tmp = tmp+"0"

    res += tmp[::-1]

if not res:
    print(0)
else:
    print(res)
