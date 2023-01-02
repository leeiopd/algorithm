# 자신을 평가한 점수가 유일한 최고 또는 최저점이라면 제외하고 평균 구함

def checkMinMax(x, y, scores, L):
    Min = scores[y][x]
    Max = scores[y][x]

    for i in range(L):
        if y == i:
            continue
        Min = min(scores[i][x], Min)
        Max = max(scores[i][x], Max)

    if scores[y][x] != Min and scores[y][x] != Max:
        return True

    for i in range(L):
        if y == i:
            continue
        if scores[i][x] == scores[y][x]:
            return True
    return False


def getGrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'


def solution(scores):
    L = len(scores)
    answer = ''

    for i in range(L):
        add = 0
        cnt = L
        for j in range(L):
            if i == j:
                if checkMinMax(i, j, scores, L):
                    add += scores[j][i]
                else:
                    cnt -= 1
            else:
                add += scores[j][i]

        answer += getGrade(add/cnt)

    return answer


print(solution([[90, 90, 90, 90], [70, 70, 70, 70],
      [90, 90, 90, 90], [70, 70, 70, 70]]))
