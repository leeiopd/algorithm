num_dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def solution(s):
    answer = ''
    L = len(s)
    for i in range(L):
        if s[i].isdecimal():
            answer += s[i]
            continue
        tmp = ''
        for j in range(i, L):
            tmp += s[j]
            if tmp in num_dic:
                answer += num_dic[tmp]
                break

    return int(answer)


def solution2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
