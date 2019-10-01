def solution(prices):
    answer = [0] * len(prices)
    k = 0
    while k < len(prices)-1:
        price = prices[k]
        cnt = 0
        for i in prices[k+1:]:
            if price > i:
                cnt += 1
                break
            else:
                cnt += 1
        answer[k] = cnt
        k += 1

    return answer
