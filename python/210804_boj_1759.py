from itertools import combinations

L, C = map(int, input().split())
alphas = input().split()
alphas.sort()
aeiou = ('a', 'e', 'i', 'o', 'u')

# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
# 알파벳이 암호에서 증가하는 순서로 배열

res = set()
for com in combinations(range(C), L):
    tmp = ""
    aeiouCnt = 0
    notAeiouCnt = 0
    for c in com:
        if alphas[c] in aeiou:
            aeiouCnt += 1
        else:
            notAeiouCnt += 1
        tmp += alphas[c]
    if aeiouCnt < 1 or notAeiouCnt < 2:
        continue
    res.add(tmp)

res = list(res)
res.sort()
for r in res:
    print(r)
