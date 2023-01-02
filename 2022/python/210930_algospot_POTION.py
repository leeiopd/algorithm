c = int(input())


def get_gcd(p, q):
    if q == 0:
        return p
    return get_gcd(q, p % q)


def get_r_gcd(r_list):
    for i in range(1000, 0, -1):
        flag = 1
        for r in r_list:
            if get_gcd(i, r) != i:
                flag = 0
                break
        if flag:
            return i


def get_answer(r_list, p_list, n):
    cnt = 1
    while True:
        flag = 1
        for i in range(n):
            if r_list[i] * cnt < p_list[i]:
                flag = 0
                break
        if flag:
            break
        cnt += 1

    temp = [0] * n
    for i in range(n):
        temp[i] = r_list[i] * cnt - p_list[i]
    return temp


for _ in range(c):
    n = int(input())

    # 필요한 재료 량
    r_list = list(map(int, input().split()))
    r_gcd = get_r_gcd(r_list)

    gcd_r_list = [r // r_gcd for r in r_list]

    p_list = list(map(int, input().split()))

    answer = get_answer(gcd_r_list, p_list, n)

    print(" ".join(map(str, answer)))
