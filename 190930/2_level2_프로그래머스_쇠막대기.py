def solution(arrangement):
    answer = 0
    level = 0
    L = len(arrangement)
    for i in range(L):
        if arrangement[i] == '(':
            level += 1
        elif arrangement[i] == ')':
            level -= 1
            if arrangement[i-1] == '(':
                answer += level
            else:
                answer += 1
    return answer
