def makeZip(arr, cnt):
    global L
    for i in range(0, L, cnt):
        for j in range(0, L, cnt):
            tmp = arr[i][j]
            flag = 1
            for y in range(i, i+cnt):
                if not flag:
                    break
                for x in range(j, j+cnt):
                    if tmp != arr[y][x]:
                        flag = 0
                        break
            if flag:
                for y in range(i, i+cnt):
                    for x in range(j, j+cnt):
                        if arr[y][x] < 0:
                            arr[y][x] = -1 * (cnt**2)
                        else:
                            arr[y][x] = (cnt**2)
    return arr


def solution(arr):
    global L
    answer = [0] * 2
    L = len(arr)

    for y in range(L):
        for x in range(L):
            if arr[y][x]:
                arr[y][x] = 1
            else:
                arr[y][x] = -1

    cnt = 1
    while cnt < L:
        cnt *= 2
        arr = makeZip(arr, cnt)

    zeros = [0] * (L*L+1)
    ones = [0] * (L*L+1)

    for y in range(L):
        for x in range(L):
            if arr[y][x] < 0:
                zeros[abs(arr[y][x])] += 1
            else:
                ones[arr[y][x]] += 1

    for i in range(1, L*L+1):
        if zeros[i]:
            answer[0] += zeros[i]//i
        if ones[i]:
            answer[1] += ones[i]//i

    return answer


print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], ]))
