import sys
from collections import deque
sys.stdin = open("1_input.txt")
'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.

사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.

단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.

예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.


[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    queue = deque()
    queue.append([N, 0])
    visited = [N]

    while queue:
        N, cnt = queue.popleft()
        if N == M:
            result = cnt
            break

        else:
            for i in range(4):
                if M in visited:
                    break
                if i == 0 and N*2 not in visited:
                    visited.append(N*2)
                    queue.append([N * 2, cnt + 1])
                if i == 1 and N+1 not in visited:
                    visited.append(N+1)
                    queue.append([N + 1, cnt + 1])
                if i == 2 and N-1 not in visited:
                    if N - 1 >= 0:
                        visited.append(N-1)
                        queue.append([N - 1, cnt + 1])
                    else:
                        break
                if i == 3 and N-10 not in visited and N - 10 >= 0:
                    visited.append(N-10)
                    queue.append([N - 10, cnt + 1])
    print("#{} {}" .format(case, result))