import sys
sys.stdin  = open("1_input.txt")
'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
T = int(input())


for case in range(1, T+1):
    V, E = map(int, input().split())
    route = []
    for e in range(E):
        f, t, w = map(int, input().split())
        route.append([w, f, t])
    route.sort()
    graph = [[0]]*V
    add = 0
    top = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                maps[i][j] = min(maps[i][k] + maps[k][j], maps[i][j])


    print("#{} {}" .format(case, add))
    print(graph)