def findBin(N):
    k = N % 4

    if k == 0:
        return N+1
    elif k == 1:
        return N+1
    elif k == 2:
        return N+1
    else:
        bin_N = list(map(str, '0'+bin(N)[2:]))
        L = len(bin_N)
        for i in range(L-1, -1, -1):
            if bin_N[i] == '0':
                bin_N[i] = '1'
                bin_N[i+1] = '0'

                bin_N = '0b'+''.join(bin_N)
                return int(bin_N, 2)


def solution(numbers):
    L = len(numbers)
    answer = [0] * L

    for i in range(L):
        answer[i] = findBin(numbers[i])
    return answer
