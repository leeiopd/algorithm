N = int(input())


def hanoi(n, From, notMove, To):
    if n == 1:
        move.append([From, To])
        return

    hanoi(n-1, From, To, notMove)
    move.append([From, To])
    hanoi(n-1, notMove, From, To)


move = []
hanoi(N, 1, 2, 3)

print(len(move))
for m in move:
    print(m[0], m[1])
