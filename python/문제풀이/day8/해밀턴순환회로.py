import sys
sys.stdin = open("해밀턴순환회로.txt")
'''
문제를 잘 풀기로 소문난 도경이는 모든 올림피아드 대회에 참가하고 싶어 했다.
대회에 참가하여 상이란 상은 다 타고 싶은 마음이었지만, 한 가지 걸리는 것이 있었다.
 
문제는 올림피아드 대회가 모두 해외에서 열리는 관계로 비행기 값이 굉장히 많이 들어간다는 것이다.
결국에는 집으로 다시 돌아와야 하는데, 모든 대회에 1번씩만 참가하고 집으로 돌아오는 경비를 가장 최소화하고 싶다.
도경이는 이것을 해결하지 못하면, 대회에 참가하기가 어렵게 된다.
대회는 참가하기만 하면 언제든지 알고리즘 문제를 풀 수 있기 때문에 경기를 계산하는 것 이외의 사항은 고려하지 않아도 된다.

첫 줄은 참가하는 대회의 수 N(1≤N≤10)을 입력 받는다. 이때, 출발지(집)는 1번으로 한다.
둘째 줄은 N*N 크기의 대회 개최지와 개최지를 이동하는 항공료(0≤항공료<100)가 나온다. 
각 항공료는 한 칸의 공백으로 구분된다.
만약에 개최지에서 개최지로 이동할 수 있는 항공로가 없다면 항공료의 값을 0으로 표시한다.

집에서 출발하여 전체 대회를 모두 참가하고 돌아올 때, 최소의 항공료를 출력한다.
'''
N = int(input())

location = []

for n in range(N):
    location.append(list(map(int, input().split())))


visited = [0] + [-1] * (N-1) + [0]
result = 99999999999999999
def travel(k=1):
    global visited, result
    # add = 0
    # for i in range(k):
    #     add += location[visited[i+1]][visited[i]] # 0 2 3 1 5 4 0
    #     if add > result:                            # 23 + 14 + 3 + 13 + 6 + 51
    #         return

    if k == N:
        add = 0
        for i in range(N):
            if location[visited[i]][visited[i+1]] == 0:
                return
            add += location[visited[i]][visited[i+1]] # 23 + 14 + 16 + 6 + 25 + 0
            if add > result:
                return
        if add < result:
            result = add

    else:
        for i in range(N):
            if i not in visited:
                visited[k] = i
                travel(k+1)
                visited[k] = -1

travel()
print(result)