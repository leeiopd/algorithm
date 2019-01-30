'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.

첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)

3
2
2 2 4 4 1
3 3 6 6 2

'''

import sys

sys.stdin = open("01_input.txt")

T = int(input())

for i in range(1, T+1):
    n = int(input())
    lists = []
    for l in range(n):
        lists.append(list(map(int, input().split())))

    maps = [[0 for _ in range(10)] for _ in range(10)]
    # map = [[0] * 10 for i in range(10)]

    for paints in lists:
        if paints[4] == 1:
            for y in range(paints[1], paints[3]+1):
                for x in range(paints[0], paints[2]+1):
                    if maps[y][x] == 1:
                        continue
                    else:
                        maps[y][x] += 1
        if paints[4] == 2:
            for y in range(paints[1], paints[3]+1):
                for x in range(paints[0], paints[2]+1):
                    if maps[y][x] == 2:
                        continue
                    else:
                        maps[y][x] += 2
    # for k in range (n):
    #     r1, c1, r2, c2, color = map(int, input().split())
    #     for i in range(r1, r2 + 1):
    #         for j in range(c, c2+1):
    #             data[i][j] += color


    cnt = 0
    for y in range(10):
        for x in range(10):
            if maps[y][x] == 3:
                cnt += 1
    print(f'#{i} {cnt}')
