def solution(n, money):
    answer = 0
    K = len(money)
    temp = [[0, 0, 0, 0]]
    while temp:
        tmp = temp.pop()
        if tmp[0] == n:
            answer += 1
        for i in range(1, K+1):
            if tmp[0] + money[i-1] < n:
                tmp[i] += 1
                tmp[0] += money[i-1]
                tp = [0] * (K+1)
                for j in range(K+1):
                    tp[j] = tmp[j]
                temp.append(tp)
    return answer


n = int(input())
money = list(map(int, input().split()))

solution(n, money)
