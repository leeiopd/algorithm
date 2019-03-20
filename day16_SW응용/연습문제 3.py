bit = {'0':'001101',
       '1':'010011',
       '2':'111011',
       '3':'110001',
       '4':'100011',
       '5':'110111',
       '6':'001011',
       '7':'111101',
       '8':'011001',
       '9':'101111',
       }

bool_bit =  {'0':'0000',
             '1':'0001',
             '2':'0010',
             '3':'0111',
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

n_list = '0269FAC9A0'
string = []
for n in n_list:
    string += list(bool_bit[n])
result = ''

for i in range(len(string)-5):
    for k in range(9):
        flag = 0
        k = str(k)
        for j in range(i, i+6):
            if bit[k][j-i] != string[j]:
                flag = 1
                break
        if flag == 0:
            result += k + ' '
            for j in range(i, i + 6):
                string[j] = '*'


print(result)