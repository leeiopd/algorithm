N, M = map(int, input().split())

trees = list(map(int, input().split()))

end = max(trees)
start = 1


def cutTree(h):
    global M
    res = 0
    for t in trees:
        if t-h > 0:
            res += (t-h)
    return res


while start <= end:
    mid = (start+end)//2

    res = cutTree(mid)

    if res < M:
        end = mid-1
    else:
        start = mid+1

print(end)
