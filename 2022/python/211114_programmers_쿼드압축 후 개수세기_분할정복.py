
def makeZip(y, x, N, arr):
    global answer
    init = arr[y][x]
    n = N//2
    for i in range(y, y+N):
        for j in range(x, x+N):
            if init != arr[i][j]:
                makeZip(y, x, n, arr)
                makeZip(y, x+n, n, arr)
                makeZip(y+n, x, n, arr)
                makeZip(y+n, x+n, n, arr)
                return
    answer[init] += 1


def solution(arr):
    global answer
    answer = [0] * 2
    L = len(arr)
    makeZip(0, 0, L, arr)
    return answer


print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [
      0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], ]))
