def solution(numbers):
    answer = 0
    numsCheck = [0] * 10
    for number in numbers:
        numsCheck[number] += 1

    for i in range(10):
        if numsCheck[i]:
            continue
        answer += i

    return answer


def solution2(numbers):
    answer = 45 - sum(numbers)
    return answer
