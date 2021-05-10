import sys

sys.stdin = open("03_input.txt")

T = int(input())

def game(a, b):
    card1 = cards[a-1]
    card2 = cards[b-1]
    if card2 == 1 and card1 == 3:
        return [b]
    elif card2 == 2 and card1 == 1:
        return [b]
    elif card2 == 3 and card1 == 2:
        return [b]
    return [a]

def diff(people_num):
    if len(people_num) > 2:
        h = (1 + len(people_num)) // 2
        people_num1 = diff(people_num[:h])
        people_num2 = diff(people_num[h:])
        people_num = people_num1 + people_num2
        people_num = diff(people_num)
        return people_num
    
    elif len(people_num) == 1:
        return people_num

    people_num = game(people_num[0], people_num[1])
    return people_num

for case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    people_num = [ x for x in range(1, N+1)]
    result = diff(people_num)
        
    print(f'#{case} {result.pop()}')