N, S = map(int, input().split())
nums = list(map(int, input().split()))
res = 0


def DFS(idx, add):
    global N, S, res
    if idx == N:
        return

    add += nums[idx]

    if add == S:
        res += 1

    DFS(idx+1, add)
    DFS(idx+1, add-nums[idx])


DFS(0, 0)
print(res)
