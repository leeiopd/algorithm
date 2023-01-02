# n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
#   그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
#   n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
#   이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
#   이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
from collections import deque
case = int(input())

for _ in range(case):
    A, B = map(int, input().split())
    visited = set()
    queue = deque()
    queue.append((A, ""))

    while True:
        Q, command = queue.popleft()

        if Q == B:
            print(command)
            break

        doubleQ = (Q*2) % 10000
        if doubleQ not in visited:
            visited.add(doubleQ)
            queue.append((doubleQ, command + "D"))

        mQ = Q-1 if Q != 0 else 9999
        if mQ not in visited:
            visited.add(mQ)
            queue.append((mQ, command + "S"))

        LQ = (Q % 1000) * 10 + (Q//1000)
        if LQ not in visited:
            visited.add(LQ)
            queue.append((LQ, command + "L"))

        RQ = (Q % 10) * 1000 + (Q//10)
        if RQ not in visited:
            visited.add(RQ)
            queue.append((RQ, command + "R"))
