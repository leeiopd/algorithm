'''
2016년은 삼성전자가 러시아 현지법인을 설립한지 20주년이 된 해이다. 이를 기념해서 당신은 러시아 국기를 만들기로 했다.

먼저 창고에서 오래된 깃발을 꺼내왔다. 이 깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 파란색, 빨간색 중 하나로 칠해져 있다.

당신은 몇 개의 칸에 있는 색을 다시 칠해서 이 깃발을 러시아 국기처럼 만들려고 한다. 다음의 조건을 만족해야 한다.

위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.

이렇게 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여라.


          

첫 번째 예제이다. 왼쪽에 있는 그림이 입력이다. 중간에 있는 그림에 X가 적힌 칸들을 새롭게 색칠하여 오른쪽에 있는 그림과 같은 깃발을 만들면 최적이다.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N,M(3≤N,M≤50)이 공백으로 구분되어 주어진다.

다음 N개의 줄에는 M개의 문자로 이루어진 문자열이 주어진다. i번 째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색을 의미한다.

‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색을 의미한다. ‘W’, ‘B’, ‘R’외의 다른 문자는 입력되지 않는다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값을 구하여 T 줄에 걸쳐서 출력한다.
'''
import sys
sys.stdin = open('4613.txt')

T = int(input())


def powerSet(x=0):
    if x == 3:
        if sum(pTemp) == N-2:
            tmp = [0] * 3
            if pTemp[1]:
                for i in range(3):
                    tmp[i] = pTemp[i]
                floorSet.append(tmp)
    else:
        for i in range(N - 1):
            pTemp[x] = i
            if sum(pTemp) <= N-2:
                powerSet(x + 1)
            pTemp[x] = 0


for case in range(1, T + 1):
    N, M = map(int, input().split())
    maps = []
    for n in range(N):
        maps.append(list(map(str, input())))

    cnt = 0

    for m in range(M):
        if maps[0][m] != 'W':
            cnt += 1
        if maps[N-1][m] != 'R':
            cnt += 1

    colorTemp = [0] * N
    for i in range(1, N - 1):
        temp = [0, 0, 0]
        for j in range(M):
            if maps[i][j] == 'W':
                temp[0] += 1
            elif maps[i][j] == 'B':
                temp[1] += 1
            else:
                temp[2] += 1
        colorTemp[i] = temp
    colorTemp.pop(0)
    colorTemp.pop(-1)

    pTemp = [0] * 3
    floorSet = []
    powerSet()
    tmpCnt = 999999999999999999999999
    while floorSet:
        floor = floorSet.pop(0)
        Wfloor = floor[0]
        Bfloor = Wfloor + floor[1]
        Rfloor = Bfloor + floor[2]
        fcnt = 0
        for w in range(1, Wfloor + 1):
            for m in range(M):
                if maps[w][m] != 'W':
                    fcnt += 1
        if fcnt > tmpCnt:
            continue

        for b in range(Wfloor + 1, Bfloor+1):
            for m in range(M):
                if maps[b][m] != 'B':
                    fcnt += 1
        if fcnt > tmpCnt:
            continue

        for r in range(Bfloor + 1, N - 1):
            for m in range(M):
                if maps[r][m] != 'R':
                    fcnt += 1
        if fcnt > tmpCnt:
            continue

        if fcnt < tmpCnt:
            tmpCnt = fcnt
    result = tmpCnt + cnt
    print('#{} {}'.format(case, result))
