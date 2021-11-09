
def get_n(N):
    cnt = 0
    for i in range(1, N+1):
        if N % i:
            continue
        cnt += 1
    return cnt


def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        N = get_n(i)
        if N % 2:
            answer -= i
        else:
            answer += i
    return answer


# 약수가 홀수개인 모든 수는 제곱수
def solution2(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer
