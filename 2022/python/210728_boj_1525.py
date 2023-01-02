from collections import deque

insNum = ""
for _ in range(3):
    insNum += "".join(input().split())

idx = insNum.index("0")

match = "123456780"


def change(idx, nums):
    U = D = R = L = ""
    if idx > 2:
        tmp = list(nums)
        tmp[idx - 3], tmp[idx] = tmp[idx], tmp[idx - 3]
        U = "".join(tmp)

    if idx < 6:
        tmp = list(nums)
        tmp[idx + 3], tmp[idx] = tmp[idx], tmp[idx + 3]
        D = "".join(tmp)

    if idx < 8 and idx % 3 < 2:
        tmp = list(nums)
        tmp[idx + 1], tmp[idx] = tmp[idx], tmp[idx + 1]
        R = "".join(tmp)

    if idx > 0 and idx % 3 > 0:
        tmp = list(nums)
        tmp[idx - 1], tmp[idx] = tmp[idx], tmp[idx - 1]
        L = "".join(tmp)

    return U, D, R, L


queue = deque()
queue.append([idx, insNum, 0])
res = -1
visited = set()

while queue:
    idx, nums, cnt = queue.popleft()

    if nums == match:
        res = cnt
        break

    U, D, R, L = change(idx, nums)
    if U and U not in visited:
        queue.append([idx-3, U, cnt+1])
        visited.add(U)

    if D and D not in visited:
        queue.append([idx+3, D, cnt+1])
        visited.add(D)

    if R and R not in visited:
        queue.append([idx+1, R, cnt+1])
        visited.add(R)

    if L and L not in visited:
        queue.append([idx-1, L, cnt+1])
        visited.add(L)

print(res)
