arr = [0, 5, 4, 0, 6, 0]

check = [0] * 7

result = "None"
triplet = 0
baby = 0
def babygin(arr):
    global result, triplet, baby

    A = arr[:3]
    B = arr[3:]

    if A[0] == A[1] and A[1] == A[2]:
        triplet = 1

    elif B[0] == B[1] and B[1] == B[0]:
        triplet = 1

    if A[0] + 1 == A[1] and A[1] + 1 == A[2]:
        baby = 1
    elif B[0] + 1 == B[1] and B[1] + 1 == B[2]:
        baby = 1


def game(arr, k):
    global check
    if k == 5:
        print(arr)
        babygin(arr)
    else:
        for i in range(5):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            game(arr, k+1)
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


k = 0
game(arr, k)
if triplet and baby:
    result = "baby-gin"
elif triplet:
    result = "triplet"
elif baby:
    result = "baby"

print(result)