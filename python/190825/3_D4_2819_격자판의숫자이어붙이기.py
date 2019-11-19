'''
4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.

격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,

각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.

이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.

격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스마다 4개의 줄에 걸쳐서, 각 줄마다 4개의 정수로 격자판의 정보가 주어진다.


[출력]

각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 격자판을 이동하며 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 출력한다.
'''
import sys
sys.stdin = open('2891.txt')

T = int(input())


def dfs(x, y, deep, nums):
    global resultList
    if deep == 7:
        # 시간 단축을 위하여 결과값을 dfs에 들고다니며 처리하자
        if nums not in resultList:
            resultList.append(nums)

    else:
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < 4 and 0 <= Y < 4:
                dfs(X, Y, deep+1, nums+maps[Y][X])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for case in range(1, T+1):
    maps = []
    for i in range(4):
        maps.append(list(map(str, input().split())))
    temp = [-1] * 7
    resultList = []
    for y in range(4):
        for x in range(4):
            dfs(x, y, 1, maps[y][x])
    result = len(resultList)

    print('#{} {}'.format(case, result))
