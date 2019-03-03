'''
해야 할 V개의 작업이 있다. 이들 중에 어떤 작업은 특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자.

이런 작업의 선행 관계를 나타낸 그래프가 주어진다.

이 그래프에서 각 작업은 하나씩의 정점으로 표시되고 선행 관계는 방향성을 가진 간선으로 표현된다.

단, 이 그래프에서 사이클은 존재하지 않는다 (사이클은 한 정점에서 시작해서 같은 정점으로 돌아오는 경로를 말한다).

아래 그림은 이런 그래프의 한 예다.


이 그래프에서 작업 1은 작업 4가 끝나야 시작할 수 있다.

작업 6은 작업 5와 작업 7이 끝나야 할 수 있다.

이 그래프에서는 사이클이 없다.

김과장은 선행 관계가 주어진 작업군을 한 번에 하나의 작업씩 처리해서 다 끝내려 한다.

위에서 예를 든 작업군에 대해서 이런 일을 한다면 아래의 순서로 처리할 수 있다.

8, 9, 4, 1, 5, 2, 3, 7, 6

또한 아래의 순서도 가능하다.

4, 1, 2, 3, 8, 5, 7, 6, 9

아래의 순서는 가능하지 않다.

4, 1, 5, 2, 3, 7, 6, 8, 9

이 순서에서는 작업 5가 작업 8보다 먼저 처리되는데, 위 그래프에서 주어진 선행 관계에서는 작업 5는 작업 8이 끝나야 시작할 수 있어 이 순서로 끝내는 것은 가능하지 않다.

V개의 작업과 이들 간의 선행 관계가 주어질 때, 한 사람이 한 번에 하나씩 일을 할 수 있는 작업 순서를 찾는 프로그램을 작성하라.

가능한 작업 순서는 보통 여러 가지가 있으므로 여러분은 이들 중 하나만 제시하면 된다.

사이클이 있는 그래프는 입력에서 주어지지 않으므로 이런 경우에 대한 에러 처리는 고려하지 않아도 좋다.

사이클이 없는 그래프에서 가능한 순서는 항상 존재한다.

[제약 사항]

그래프에서 정점의 총 수 V는 5≤V≤1000.

[입력]

10개의 테스트 케이스가 주어진다.

20줄에 걸쳐, 두 줄에 테스트 케이스 하나씩 제공된다.

각 케이스의 첫줄에는 그래프의 정점의 총 수 V와 간선의 총 수 E가 주어진다.

그 다음 줄에는 E개 간선이 나열된다.

간선은 간선을 이루는 두 정점으로 표기된다.

예를 들어, 정점 5에서 28로 연결되는 간선은 “5 28”로 표기된다.

정점의 번호는 1부터 V까지의 정수값을 가지며, 입력에서 이웃한 수는 모두 공백으로 구분된다.

[출력]

총 10줄에 10개의 테스트케이스 각각에 대한 답을 출력한다.

각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음 작업 순서를 기록한다.

작업 순서는 V개 정수를 공백을 사이에 두고 나열하는 것이다.
'''

import sys

sys.stdin = open('08_input.txt')


# def work(maps, start):
#     global V, result, visited, in_check
#     if visited[start] == 0:
#         visited[start] += 1
#         result.append(start)

#     for i in range(1, V+1):
#         if maps[i][start] == 1 and in_check[i] != 0:
#             in_check[i] -= 1
#             maps[i][start] -= 1
#             start = i
#             work(maps, start)

# 0 1 0
# 0 0 0
# 1 0 0

# 1 0 1

# 2 -> 1 -> 3

def work(maps, start):
    global V, result, visited, in_check

    if visited[start] == 1 or len(result) == V:
        return

    visited[start] = 1
    result.append(start)
    for i in range(1,V+1):
        if maps[i][start] == 1:
            start = i
            in_check[i] -= 1
            work(maps, start)



T = 10
for t in range(1, T+1):
    V, E = map(int,input().split()) # V: 정점, E: 간선

    line = list(map(int, input().split()))
    maps = [[0 for x in range(V+1)] for y in range(V+1)]

    for e in range(E):
        x = line[e * 2]
        y = line[(e * 2) + 1]
        maps[y][x] = 1

    result = ''
    in_check = [0] * (V+1) # 진입차수 저장
    for i in range(1, V+1):
        in_check[i] = sum(maps[i])

    result = []
    visited = [0] * (V+1)
    while len(result) < V:
        for i in range(1, V+1):
            if in_check[i] == 0 and visited[i] != 1:
                work(maps, i)

    ans = ' '.join(map(str, result))
    print(f'#{t} {ans}')
