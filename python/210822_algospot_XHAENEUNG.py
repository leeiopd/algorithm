N = int(input())

s2n = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
       'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

n2s = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
       5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

for _ in range(N):
    row = input().split()
    a = s2n[row[0]]
    b = s2n[row[2]]

    answer = ''
    collect = ''

    if row[1] == '+':
        if a + b > 10:
            print("No")
            continue
        answer = row[4]
        collect = n2s[a+b]
    elif row[1] == '-':
        if a - b < 0:
            print("No")
            continue
        answer = row[4]
        collect = n2s[a-b]
    elif row[1] == '*':
        if a * b > 10:
            print("No")
            continue
        answer = row[4]
        collect = n2s[a*b]

    if len(answer) != len(collect):
        print("No")
        continue

    check_answer = {}
    for ans in answer:
        if ans not in check_answer:
            check_answer[ans] = 1
        else:
            check_answer[ans] += 1

    check_collect = {}
    for col in collect:
        if col not in check_collect:
            check_collect[col] = 1
        else:
            check_collect[col] += 1

    if check_answer == check_collect:
        print("Yes")
    else:
        print("No")
