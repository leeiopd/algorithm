import sys

sys.stdin = open("15_input.txt")

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

def find_code(codes):
    global password
    for y in range(N):
        for x in range(M):
            if codes[y][x] != '0':
                j = x
                while True:
                    if codes[y][j] == '0':
                        break
                    password += codes[y][j]
                    codes[y][j] = '0'
                    j += 1
                return

bool_table = {'0':'0000',
              '1':'0001',
              '2':'0010',
              '3':'0011',
              '4':'0100',
              '5':'0101',
              '6':'0110',
              '7':'0111',
              '8':'1000',
              '9':'1001',
              'A':'1010',
              'B':'1011',
              'C':'1100',
              'D':'1101',
              'E':'1110',
              'F':'1111',
              }

for case in range(1, T+1):
    N, M = map(int, input().split())
    codes = []
    for n in range(N):
        code = list(map(str, input()))
        codes.append(code)
    result_list = []
    pass_list = []

    while True:
        password = ''
        find_code(codes)
        if not password:
            break
        if password not in pass_list:
            pass_list.append(password)

    while pass_list:

        result = 0

        password = pass_list.pop(0)
        password2 = ''
        for p in password:
            password2 += bool_table[p]
        password3 = ''
        for i in range(len(password2)-1, -1, -1):
            if password2[i] != '0':
                for j in range(i, i-56, -1):
                    password3 += password2[j]
                break
        password3 = password3[::-1]
        cnt = 0
        k = 1
        result = 0
        odd = 0
        even = 0
        while cnt < 56:
            pass_code = password3[cnt:cnt+7]
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
            if result not in result_list:
                result_list.append(result)


    if not result_list:
        print(case, 0)
    else:
        print(case, sum(result_list))