import sys
#push X: 정수 X를 큐에 넣는 연산이다.
#pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 큐에 들어있는 정수의 개수를 출력한다.
#empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
#front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        queue.append(int(order[1]))
    elif order[0] == 'pop':
        print(queue.pop(0) if queue else -1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        print(0 if queue else 1)
    elif order[0] == 'front':
        print(queue[0] if queue else -1)
    elif order[0] == 'back':
        print(queue[-1] if queue else -1)