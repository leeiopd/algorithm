# 부분 집합 출력 함수
def process_solution(a, k):
    for i in range(1, k+1):
        print(data[a[i]], end=" ")
    print()

# 입력 함수
def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands


# backtrack 반복 실행 함수
def backtrack(a, k, input):     # a: 저장된 메모리 공간, k : 부분집합 하나의 완성도, input : 집합 원소 개수
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)

    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100      # 함수가 작동되면서 저장될 메모리 공간 넉넉히 할당
NMAX = 100
data = [0, 1, 2, 3]      # 부분집합을 구할 집합 원소 (index 1~3)
a = [0] * NMAX           # 부분집합들이 저장할 메모리 공간 넉넉히 할당
backtrack(a, 0, 3)