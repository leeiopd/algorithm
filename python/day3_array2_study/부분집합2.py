arr = [1, 2, 3, 4]
n = len(arr)

for i in range(1 << n): # (1 << n) == 2 ** n -> 16
    for j in range(n):
        print(f'n: {n}, j: {j}')
        if i & ( 1 << j ):
            print(f'1<<j: {1<<j}')
    #         arr[j]
    #         print(arr[j], end=",")
    #
    # print()