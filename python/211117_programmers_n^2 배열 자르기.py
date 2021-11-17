def solution(n, left, right):
    answer = [0] * (right-left+1)

    for i in range(n):
        if (i+1)*n < left:
            continue
        if i*n > right:
            break
        for j in range(n):
            if left <= n*i + j <= right:
                if i >= j:
                    answer[n*i + j - left] = i+1
                else:
                    answer[n*i + j - left] = j+1
    return answer
