# 비트마스크 _ 극대 안정 집합

# 안정적 : 한 상자에 넣어도 폭발하지 않는 물질의 집합
# 물질이 하나만 있는 집합은 항상 안정적

# 극대 안정 집합 : 물질을 하나라도 추가하면 폭발이 일어나는 집합

# 극대 안정 집합의 개수 구하기

N = int(input())

explodes = [0] * N


def isStable(set):
    for i in range(N):
        if((set & (1 << i)) and (set & explodes[i])):
            return False
    return True


def countStableSet():
    ret = 0

    cnt = 1
    while cnt < (1 << N):
        if not isStable(cnt):
            continue

        canExtend = False

        for add in range(N):
            if(cnt & (1 << add)) == 0 and (explodes[add] & cnt) == 0:
                canExtend = True
                break
        if not canExtend:
            ret += 1
        cnt += 1
    return ret
