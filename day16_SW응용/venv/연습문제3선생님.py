



code = [[[[[[x for x in range(2)]for x in range(2)]for x in range(2)]for x in range(2)]for x in range(2)]for x in range(2)]

code[]




t = []
arr = '0269FAC9A0'

ans = []
pos = -1

for i in range(len(arr)):
    makeT(aToh(arr[i]))


for i in range(len(t)-1, -1, -1):
    if t[i] == 1:
        pos = i
        break


while pos - 6 > 0:
    x = code[t[pos-5][t[pos-4]][t[pos-3]][t[pos-2]][t[pos-1]][t[pos]]]
    ans.append(x)
    pos -= 6

for i in range(len(ans)):
    print(ans,pop(), end="")
print()