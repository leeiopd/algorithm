def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    M = len(p) # 찾을 패턴의 길이
    N = len(t) # 전체 텍스트의 길이

    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M :
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패

t = "TTTTA"
p = "TTA"

print(BruteForce(p, t))
print(t.find(p))


def BruteForce2(text, pattern):
    for i in range(len(text) - len(pattern) + 1): # 패턴의 길이 만큼만 남을때까지 for문을 돌겠다.
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt += 1
        if(cnt >= len(pattern)):
            return i
    return -1

text ="TTTTAACCA"
pattern = "TTA"

print(BruteForce2(text, pattern))