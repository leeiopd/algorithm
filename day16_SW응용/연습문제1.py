list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,   1, 0, 0, 0, 0, 0, 0, 1, 1, 0,   0, 0, 0, 0, 0, 1, 1, 1, 1, 0,   0, 1, 1, 0, 0, 0, 0, 1, 1, 0]

bits = []
cnt = 0
while len(list)>cnt:
    A = list[cnt:cnt+10]
    bits.append(A)
    cnt += 10
print(bits)
for bit in bits:
    result = 0
    b_cnt = 0
    for i in range(9, -1, -1):
        if bit[i] == 1:
            k = 2**b_cnt
            result += k
        b_cnt += 1
    print(result)


'''
for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + arr[j]
    print(n, end=" ")
print()

'''