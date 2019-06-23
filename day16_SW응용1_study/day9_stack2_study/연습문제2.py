powerset = [0,1,2,3,4,5,6,7,8,9,10]

stack = [0] * 100

set_result = [0] * 11


def setfun(set_result, k, num):
    if k==num:
        check(set_result)

    else:
        k += 1
        for i in range(2):
            set_result[k] = i
            setfun(set_result, k, num)


def check(set_result):
    result = []
    for i in range(len(set_result)):
        if set_result[i] == 1:
           result.append(int(powerset[i]))

    if sum(result) == 10:
        print(result)


setfun(set_result, 0, 10)