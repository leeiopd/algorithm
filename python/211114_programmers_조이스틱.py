from collections import deque


def strToASCII(n):
    return ord(n)


def solution(name):
    L = len(name)
    name = list(map(strToASCII, list(name)))
    nameSpace = [65] * L

    visited = [0] * L

    for i in range(L):
        nameSpace[i] = min(abs(name[i]-65), abs(91 - name[i]))
        if nameSpace[i]:
            visited[i] = 1

    queue = deque()
    queue.append([visited, 0, 0])

    answer = L-1
    while queue:
        tmp, idx, cnt = queue.popleft()

        copyTmp = [x for x in tmp]
        copyTmp[idx] = 0

        if sum(copyTmp) == 0:
            answer = min(answer, cnt)
            continue

        if cnt > L:
            continue

        if idx+1 < L:
            queue.append([copyTmp, idx+1, cnt+1])
        if idx == 0:
            queue.append([copyTmp, L-1, cnt+1])
        else:
            queue.append([copyTmp, idx-1, cnt+1])

    return sum(nameSpace) + answer


print(solution("BBBAAAB"))
