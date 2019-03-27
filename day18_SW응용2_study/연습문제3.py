arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power = [0] * 10

def powerset(k=0):
    if k == len(power):
        result = []
        for i in range(len(power)):
            if power[i] == 1:
                result.append(arr[i])
        if sum(result) == 10:
            print(result)
        return

    else:
        add = 0
        for i in range(k):
            if power[i] == 1:
                add += arr[i]
            if add > 10:
                return



        for i in range(2):
            power[k] = i
            powerset(k+1)

powerset()