

C = int(input())


def bit_count_recursion(n):
    # 1 의 개수를 count
    if n:
        # 맨 끝 한자리를 재귀를 이용하여 확인후 count
        return (n & 1) + bit_count(n >> 1)
    return 0


def bit_count(n):
    cnt = 0
    while n > 0:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt


def graduate(semester, taken):
    # 졸업까지 남은 학기 return
    global N, K, M, L, memo, prerequisites, opened_lectures, MAX
    # N : 전공 과목 수
    # K : 들어야할 과목 수
    # M : 학기 수
    # L : 한 학기 당 최대 수강 과목 수

    # 이수과목 수 >= 남은 과목 수
    if bit_count(taken) >= K:
        # 졸업
        return 0
    # 이수과목 수 < 남은 과목수, 지난 학기수 == 총 학기수
    # M 학기까지 공부했지만, 남은 과목수가 있다 -> 졸업 X
    elif semester == M:
        return MAX

    # 아직 남은 학기가 있다

    # memorization
    if memo[semester][taken]:
        return memo[semester][taken]

    res = MAX

    # taken : 수강한 수업 bitmask
    # can_take : 수강한 수업의 bitmask 를 이용하여, 학기별 개설과목 전체의 선수강 가능 여부 확인
    can_take = opened_lectures[semester] & ~taken

    for i in range(N):
        # 각 과목 별 '이번학기 수강 가능' and '선수강 과목을 수강하지 않음' -> 수강 불가
        if (can_take & (1 << i)) and (taken & prerequisites[i]) != prerequisites[i]:
            can_take &= ~(1 << i)

    # while 문 내 take 모양 만들어주기 ( take -1 로 while 문 진행)
    take = can_take + 1

    while take:
        # 수강 가능한 과목을 하나씩 미수강
        take = (take - 1) & can_take

        # 이번학기 최대 수강 과목수보다 적으면
        if bit_count(take) <= L:
            # 학기 이수, 경우의 수 진행
            # (taken | take) => 이전 학기 이수과목 + 이번학기 이수과목
            res = min(res, graduate(semester+1, taken | take) + 1)

    # take == 0 일 경우
    res = min(res, graduate(semester+1, taken))

    # memorization
    memo[semester][taken] = res

    return res


for _ in range(C):
    MAX = 987654321

    N, K, M, L = map(int, input().split())

    prerequisites = []
    for _ in range(N):
        pres = list(map(int, input().split()))[1:]

        # 선수과목을 idx 로 하는 bitmask 생성
        pres_bit = 0
        for p in pres:
            pres_bit |= (1 << p)

        prerequisites.append(pres_bit)

    opened_lectures = []
    for _ in range(M):
        lectures = list(map(int, input().split()))[1:]

        # 개설되는 과목을 idx 로 하는 bitmask 생성
        lec_bit = 0
        for l in lectures:
            lec_bit |= (1 << l)

        opened_lectures.append(lec_bit)

    # 학기 * 전공 과목수 만큼 2x2 memoArray 생성
    memo = [[0] * (1 << N) for _ in range(M)]

    ans = graduate(0, 0)

    if ans != MAX:
        print(ans)
    else:
        print("IMPOSSIBLE")
