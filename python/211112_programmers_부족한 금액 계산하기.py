def solution(price, money, count):
    price_sum = 0
    for i in range(1, count+1):
        price_sum += (price * i)
    answer = price_sum - money
    if answer < 0:
        return 0
    return answer
