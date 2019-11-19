import sys

sys.stdin = open("10_input.txt")


T = int(input())

def check(x_long, y_long):
    global maps
    flag = 0
    for y_start in range(N-y_long+1):
        if flag == 99:
            y_start -= 1
            break
        for x_start in range(N-x_long+1):
            if flag == 99:
                x_start -= 1
                break
            flag = 0
            cnt = 0

            for y in range(y_start, y_start+y_long):
                if flag == 1:
                    break
                for x in range(x_start, x_start + x_long):
                    if maps[y][x] == 0:
                        flag = 1
                        break
                    else:
                        cnt += 1
            if cnt == x_long*y_long:
                flag = 99



    if flag == 99:
        for y in range(y_start, y_start + y_long):
            for x in range(x_start, x_start + x_long):
                maps[y][x] = -0
        return True
    return False




    for case in range(1, T + 1):
        N = int(input())

        maps = []

        for n in range(N):
            maps.append(list(map(int, input().split())))
        result = []
        re_list = []

        for y in range(N, 0, -1):
            for x in range(N, 0, -1):
                if check(x, y):
                    re_list.append([y, x])

    for i in range(len(re_list)):
        for j in range(i+1, len(re_list)):
            if re_list[i][0] * re_list[i][1] > re_list[j][0] * re_list[j][1]:
                re_list[i], re_list[j] = re_list[j], re_list[i]

            if re_list[i][0] * re_list[i][1] == re_list[j][0] * re_list[j][1]:
                if re_list[i][0] > re_list[j][0]:
                    re_list[i], re_list[j] = re_list[j], re_list[i]

    print(f'#{case} {len(re_list)}', end=' ')
    for i in re_list:
        print(f'{i[0]} {i[1]}', end=' ')
    print()
