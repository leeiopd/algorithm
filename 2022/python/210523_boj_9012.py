import sys
N = int(sys.stdin.readline())

for i in range(N):
    tmp = list(sys.stdin.readline())
    res = 0
    for j in range(len(tmp)-1):
        if tmp[j] == '(':
            res += 1
        else:
            res -= 1
        if res < 0:
            res = -1
            break
    if res == 0:
        print("YES")
    else:
        print("NO")