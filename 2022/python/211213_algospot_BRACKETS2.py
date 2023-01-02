from collections import deque


def checkBrackets(brackets):
    ins = ["(", "{", "["]
    check = {")": "(", "}": "{", "]": "["}

    queue = deque()
    for b in brackets:
        if b in ins:
            queue.append(b)
        else:
            if not queue or queue[-1] != check[b]:
                return False
            queue.pop()
    return False if len(queue) else True


C = int(input())

for _ in range(C):
    brackets = input()
    print("YES" if checkBrackets(brackets) else "NO")
