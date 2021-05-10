T = int(input())
cnt = 0
def powerset(top=0, v_sum = 0):
    global result, cnt

    if top == N:
        cnt+=1
        add_V = 0
        add_C = 0
        for i in range(N):
            if power[i] == 1:
                add_V += V_list[i]
                if add_V > K:
                    return
                add_C += C_list[i]
        if add_C > result:
            result = add_C

    else:
        add = 0
        for i in range(top):
            if power[i] == 1:
                add += V_list[i]
                if add > K:
                    return

        add += sum(V_list[top:])
        if add < K:
            return


        for i in range(2):
            power[top] = i
            powerset(top + 1)


for case in range(1, T + 1):
    N, K = map(int, input().split())
    V_list = [0] * N
    C_list = [0] * N
    for n in range(N):
        V, C = map(int, input().split())
        V_list[n] = V
        C_list[n] = C
    power = [0] * N
    result = 0
    powerset()
    print(case, result)