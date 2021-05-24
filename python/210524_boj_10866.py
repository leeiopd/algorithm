import sys
N = int(sys.stdin.readline())
dq = []
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push_front':
        dq = [int(order[1])] + dq
    elif order[0] == 'push_back':
        dq.append(int(order[1]))
    elif order[0] == 'pop_front':
        print(dq.pop(0) if dq else -1)
    elif order[0] == 'pop_back':
        print(dq.pop() if dq else -1)
    elif order[0] == 'size':
        print(len(dq))
    elif order[0] == 'empty':
        print(0 if dq else 1)
    elif order[0] == 'front':
        print(dq[0] if dq else -1)
    elif order[0] == 'back':
        print(dq[-1] if dq else -1)