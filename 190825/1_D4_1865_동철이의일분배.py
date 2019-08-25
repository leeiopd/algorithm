'''
동철이가 차린 전자회사에는 N명의 직원이 있다.

그런데 어느 날 해야할 일이 N개가 생겼다.

동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.

직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.

여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.

직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.

우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤ N ≤ 16)이 주어진다.

다음 N개의 줄의 i번째 줄에는 N개의 정수 Pi, 1, … , i, N(0 ≤ Pi, j ≤ 100)이 주어진다.

Pi, j는 i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타낸다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

모든 일을 성공할 확률이 최대화될 때의 확률을 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력한다.


[예제 풀이]

첫번째 직원이 첫번째 일을 담당하고, 두번째 직원이 두번째 일을 담당하고, 세번째 직원이 세번째 일을 담당할 때

모든 일을 성공할 확률이 최대가 되고 그 확률은 (0.13*0.7*1.0)*100 = 9.1%가 된다.
'''
import sys
sys.stdin = open('1865.txt')

T = int(input())


def dfs(x=0, percent=100):
    global result
    # 1보다 작은 수를 계속 곱해 주니까, 가지치기 비교가 수월해 진다
    if percent <= result:
        return
    if x == N:
        if percent > result:
            result = percent

    else:
        for i in range(N):
            if i not in temp:
                temp[x] = i
                dfs(x+1, percent*(Works[x][i]/100))
                temp[x] = -1


for case in range(1, T+1):
    N = int(input())

    Works = []
    for n in range(N):
        Works.append(list(map(int, input().split())))

    result = 0
    temp = [-1] * N
    dfs()

    print('#{} {:.6f}'.format(case, result))
