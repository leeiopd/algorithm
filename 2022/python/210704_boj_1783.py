N, M = map(int, input().split())

if N < 2:
    print("1")
elif N < 3:
    if M < 7:
        print((M+1)//2)
    else:
        print(4)
else:
    if M < 5:
        print(M)
    elif M == 5:
        print(4)
    else:
        print(M - 2)
