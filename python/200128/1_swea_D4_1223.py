import sys

sys.stdin = open('1223.txt')

T = 10

for tc in range(1, T+1):
    N = input()
    inStrs = input().split("+")

    result = 0

    for inStr in inStrs:
        if len(inStr) == 1:
            result += int(inStr)

        else:
            temp = inStr.split("*")

            tempResult = 1

            for t in temp:
                tempResult *= int(t)

            result += tempResult

    print("#{} {}".format(tc, result))
