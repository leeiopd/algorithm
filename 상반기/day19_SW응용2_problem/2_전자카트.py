'''
골프장 관리를 위해 전기 카트로 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량을 구하시오.

각 구역을 이동할 때의 배터리 사용량은 표로 제공되며, 1번은 사무실을, 2번부터 N번은 관리구역 번호이다.

두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있다.

N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며 각각의 배터리 소비량은 다음과 같이 계산할 수 있다.

e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91

e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 100이하의 자연수가 주어진다. 3<=N<=10

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
import sys

sys.stdin = open("2_input.txt")

T = int(input())


def perm(k=0):
    global result
    if N-1 == k:
        check_nums = [0] + nums + [0]
        add = 0
        for i in range(N):
            f = check_nums[i]
            t = check_nums[i+1]
            add += maps[f][t]
            if add > result:
                return
        if add < result:
            result = add
        return

    else:
        for i in range(k, N-1):
            nums[i], nums[k] = nums[k], nums[i]
            perm(k+1)
            nums[i], nums[k] = nums[k], nums[i]




for case in range(1, T+1):
    N = int(input())

    maps = []
    for n in range(N):
        maps.append(list(map(int, input().split())))

    nums = [ x for x in range(1, N)]
    result = 99999999999999
    perm()
    print("#{} {}" .format(case, result))

