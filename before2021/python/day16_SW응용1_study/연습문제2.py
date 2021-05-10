hex_ten = {'A':10, 'B':11 , 'C':12, 'D':13, 'E':14, 'F':15}

nums = list(input())

bool_string = ''
result = []
for n in nums:
    if not n.isdecimal():
        n = hex_ten[n]
    n = int(n)
    bool_string = [0, 0, 0, 0]
    cnt = 0
    while cnt<4:
        k = n%2
        bool_string[cnt] = k
        n = n//2
        cnt += 1

    bool_string = bool_string[::-1]
    result += bool_string

cnt = 0
while cnt<len(result):
    k = ''.join(map(str, result[cnt:cnt+7]))
    print(k, end=' ')
    cnt += 7
