from collections import deque

N, K = map(int, input().split())

# 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

queue = deque()
queue.append(N)

MAX = 100000

time = [0] * 100001
time[N] = 0

while True:
    Q = queue.popleft()

    if Q == K:
        print(time[Q])
        break

    if Q+1 <= MAX and not time[Q+1]:
        time[Q+1] = time[Q]+1
        queue.append(Q+1)
    if Q-1 >= 0 and not time[Q-1]:
        time[Q-1] = time[Q]+1
        queue.append(Q-1)
    if Q*2 <= MAX and not time[Q*2]:
        time[Q*2] = time[Q]+1
        queue.append(Q*2)
