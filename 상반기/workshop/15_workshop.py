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
result_cnt = 0
for case in range(1, T+1):
    N, M = map(int, input().split())
    codes = []
    result = 0
    for n in range(N):
        ins = input()
        if ins in codes:
            continue
        codes.append(ins)

    password_list = []
    for code in codes:
        password = ''
        for c in code:
            password += bool_table[c]

        cnt = 0
        in_code = ''

        flag = 0
        for i in range(len(password)):
            in_code += password[i]
            if password[i-1] == '1' and password[i] == '0':
                cnt +=1
            if cnt != 0 and cnt % 16 == 0:
                flag = 1
            if flag == 1 and password[i] == '0':
                if in_code not in password_list:
                    password_list.append(in_code)
                in_code = ''
                flag = 0
                cnt = 0



    for i in range(len(password_list)):
        cnt_f = 0
        cnt_b = -1
        while True:
            if password_list[i][cnt_f] == '0':
                cnt_f += 1
            if password_list[i][cnt_b] == '0':
                cnt_b -= 1
            if password_list[i][cnt_f] != '0' and password_list[i][cnt_b] != '0':
                password_list[i] = password_list[i][cnt_f:cnt_b+1]
                break

    password_list = list(set(password_list))

    for password in password_list:
        flag = 0
        cnt_f = 0
        while password[cnt_f] == '0':
            cnt_f += 1
        password = password[cnt_f:]


        while len(password)%56 != 0:
            password = '0' + password
        password2 = ''
        for i in range(0, len(password), len(password)//56):
            password2 += password[i]
        password = password2



        cnt = 0
        k = 1
        code_sum = 0
        odd = 0
        even = 0
        while cnt < len(password):
            pass_code = password[cnt:cnt + 7]
            print(keys[pass_code], end=', ')
            if k != 0 and k % 8 == 0:
                check_code = keys[pass_code]
            elif k % 2:
                odd += keys[pass_code]
            else:
                even += keys[pass_code]

            code_sum += keys[pass_code]
            cnt += 7
            k += 1
        print()
        if (odd * 3 + even + check_code) % 10 == 0:
            result_cnt += 1
            result += code_sum
    print(case, result)
print(result_cnt)