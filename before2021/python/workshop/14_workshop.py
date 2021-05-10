import sys

sys.stdin = open("14_input.txt")

T = int(input())

keys = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
        }

def find_code():
    global password
    for y in range(N):
        for x in range(M-1, -1, -1):
            if codes[y][x] == 1:
                for j in range(x, x-56, -1):
                    password += str(codes[y][j])
                return


for case in range(1, T+1):
    N, M = map(int, input().split())
    codes = []
    password = ''
    for n in range(N):
        code = list(map(int, input()))
        codes.append(code)
    find_code()
    password = password[::-1]
    print(password)
    cnt = 0
    k = 1
    result = 0
    odd = 0
    even = 0
    while cnt < 56:
        pass_code = password[cnt:cnt+7]
        print(keys[pass_code])
        if k == 8:
            check_code = keys[pass_code]
        elif k % 2:
            odd += keys[pass_code]
        else:
            even += keys[pass_code]

        result += keys[pass_code]

        cnt += 7
        k += 1

    if (odd*3 + even + check_code) % 10 == 0:
        print(result)
    else:
        print(0)
