'''
준환이는 N개의 서로 다른 무게를 가진 무게 추와 양팔저울을 가지고 있다.

모든 무게 추를 양팔저울 위에 올리는 순서는 총 N!가지가 있고,

여기에 더해서 각 추를 양팔저울의 왼쪽에 올릴 것인지 오른쪽에 올릴 것인지를 정해야 해서 총 2N * N!가지의 경우가 있다.

하지만 양팔 저울에 갑자기 문제가 생겨서 무게 추를 올릴 때 오른쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 더 커져서는 안 된다.

예를 들어 무게추가 총 3개, 무게가 각각 1, 2, 4 라고 하면 아래 그림처럼 총 15가지 경우가 나올 수 있다.



이런 방법으로 준환이가 양팔 저울에 모든 무게추를 올리는 방법은 총 몇 가지가 있을까?


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 첫 번째 줄에 N(1 ≤ N ≤ 9)가 주어진다.

두 번째 줄에는 각 무게추의 무게를 의미하는 N개의 자연수가 공백으로 구분되어 주어진다. 무게는 1이상 999이하이다.


[출력]

각 테스트 케이스마다 무게추를 올리는 과정에서 오른쪽 위에 올라가있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다

커지지 않는 경우의 수를 출력한다.
'''
import sys
sys.stdin = open('3234.txt')

T = int(input())


def dfs(x=0, L=0, R=0):
    global result
    # 오른쪽 저울이 무거우면 안됨
    if R > L:
        return

    # 모든 저울을 사용 하였을 때
    if x == N:
        result += 1
        return

    # 왼쪽의 합이 이미 남은 저울의 무게의 합보다 클경우
    if L >= M-L:
        # 올려진 저울에 대한 경우의 수를 계산하여 더해주고 리턴
        result += 2**(N-x)*fact(N-x)
        return

    else:
        for i in range(N):
            # 사용하지 않은 저울일 때
            if visited[i] == 0:
                # 사용하고
                visited[i] = 1
                # 왼쪽에 사용
                dfs(x+1, L + nums[i], R)
                # 오른쪽에 사용
                dfs(x+1, L, R + nums[i])
                # 내려 놓기
                visited[i] = 0


# N * (N-1) * (N-1) * .... * 2 * 1
def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)


for case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    M = sum(nums)
    visited = [0] * N
    result = 0
    dfs()
    print('#{} {}'.format(case, result))
