# 직관적인 알고리즘
# 비율이 맞을 때까지 재료들을 계속 더 넣어보는 방법

# 1. 첫번째 재료는 4숟가락을 넣어야 하는데, 7 숟가락을 넣음
#     -> 다른 재료들도 최소 7/4 배 넣어야 함
# 2. 두번째 재료는 6 x ( 7/4 ) = 10.5 숟가락 넣어야 하는데 올림하여 11 숟가락 넣음
#     -> 다른 재료들도 11/6 배 넣어야 함
# 3. 다시 첫번째 재료는 4 x ( 11/6 ) = 7.33... 숟가락을 넣어야 하는데 올림하여 8 숟가락 넣음
#     -> 다른 재료들도 ( 8/2 ) = 2 배 넣어야 함


c = int(input())


def solveSimulation(r_list, p_list, n):
    ret = [0] * n

    for i in range(n):
        ret[i] = max(r_list[i] - p_list[i], 0)
        p_list[i] += ret[i]

    while True:
        flag = 1

        for i in range(n):
            for j in range(n):
                # i 번 재료 기준, 모든 재료는 ( p_list[i] / r_list[i] = X ) 배 이상 넣어야 한다.
                # 따라서 p_list[j] 는 r_list[i] * X 이상의 정수가 되어야 한다.
                require = (p_list[i] * r_list[j] + r_list[i] - 1) // r_list[i]

                if require > p_list[j]:
                    ret[j] += require - p_list[j]
                    p_list[j] = require
                    flag = 0

        if flag:
            break
    return ret


for _ in range(c):
    n = int(input())

    # 필요한 재료 양
    r_list = list(map(int, input().split()))

    # 넣은 양
    p_list = list(map(int, input().split()))

    answer = solveSimulation(r_list, p_list, n)

    print(" ".join(map(str, answer)))
