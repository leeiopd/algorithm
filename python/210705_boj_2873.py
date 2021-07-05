import sys
input = sys.stdin.readline

R, C = map(int, input().split())

maps = []

for _ in range(R):
    maps.append(list(map(int, input().split())))

if R % 2:
    for r in range(R):
        if r % 2:
            print("L"*(C-1), end="")
        else:
            print("R"*(C-1), end="")

        if r != R-1:
            print("D", end="")
        else:
            print("D")

elif C % 2:
    for c in range(C):
        if c % 2:
            print("U"*(R-1), end="")
        else:
            print("D"*(R-1), end="")

        if c != C-1:
            print("R", end="")
        else:
            print("R")

else:
    flag_1 = maps[0][0]
    for r in range(R):
        flag_1 += sum(maps[r][1:])

    flag_2 = maps[0][0]
    for r in range(1, R):
        flag_2 += sum(maps[r])

    flag_3 = maps[-1][-1]
    for r in range(R-1):
        flag_3 += sum(maps[r])

    flag_4 = maps[-1][-1]
    for r in range(R):
        flag_4 += sum(maps[r][:-1])

    max_flag = max(flag_1, flag_2, flag_3, flag_4)

    if max_flag == flag_1:
        print("R", end="")
        for c in range(C-1):
            if c % 2:
                print("U"*(R-1), end="")
            else:
                print("D"*(R-1), end="")

            if c != C-2:
                print("R", end="")
        print()

    elif max_flag == flag_2:
        print("D", end="")
        for r in range(R-1):
            if r % 2:
                print("L"*(C-1), end="")
            else:
                print("R"*(C-1), end="")
            if r != R-2:
                print("D", end="")
        print()

    elif max_flag == flag_3:
        for r in range(R-1):
            if r % 2:
                print("L"*(C-1), end="")
            else:
                print("R"*(C-1), end="")

            if r != R-2:
                print("D", end="")
            else:
                print("D")

    else:
        for c in range(C-1):
            if c % 2:
                print("U"*(R-1), end="")
            else:
                print("D"*(R-1), end="")

            if c != C-2:
                print("R", end="")
            else:
                print("R")
