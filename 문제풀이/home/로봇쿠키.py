import sys
sys.stdin = open("로봇쿠키.txt")

T = int(input())

def perm(k=0, ssum = 0):
    global result
    add = 0
    for i in range(k):
        add += abs(cookie[i][0] - robot[i][0]) + abs(cookie[i][1] - robot[i][1])
        if add > result:
            return

    if k == N:
        add = 0
        for i in range(N):
            add += abs(cookie[i][0] - robot[i][0]) + abs(cookie[i][1] - robot[i][1])
        if add < result:
            result = add

    else:
        for i in range(k, N):
            cookie[i], cookie[k] = cookie[k], cookie[i]
            perm(k+1)
            cookie[i], cookie[k] = cookie[k], cookie[i]

for case in range(1, T+1):
    N = int(input())

    cookie_nums = list(map(int, input().split()))
    robot_nums = list(map(int, input().split()))

    cookie = [0] * N
    for i in range(N):
        x = cookie_nums[i*2]
        y = cookie_nums[i*2+1]
        cookie[i] = [x, y]

    robot = [0] * N
    for i in range(N):
        x = robot_nums[i*2]
        y = robot_nums[i*2+1]
        robot_num = i+1
        robot[i] = [x, y]

    result = 999999999999999999

    perm()
    print(result)