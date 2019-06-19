import sys
sys.stdin  = open("그래프칠하기.txt")

'''
N개의 노드로 구성된 그래프의 정보가 주어지고, 숫자 M이 주어진다.
이 때, 서로 인접한 노드들 간에는 같은 색을 칠하지 않으면서 M개의 색으로 N개의 노드를 전부 칠할 수 있는지 판단하라.
가능한 경우에는 첫 번째 노드부터 색상 번호(1 ~ M에서 선택)를 출력하고, 불가능한 경우 -1을 출력한다.
 
노드1부터 순서대로 색을 칠해야 하며 색상 번호도 낮은 번호부터 붙여 나가야 한다. 
주어진 색상을 모두 사용할 필요는 없으며 가능하면 낮은 색상 번호를 사용하여 완성하라.
즉, 6개의 색이 주어졌어도 5개의 색으로 모두 칠할 수 있으면 5개색만 사용하여야 한다.
 
그래프 정보는 triangular matrix로 주어지고, 연결되어 있는 경우 1, 연결되어 있지 않은 경우 0으로 주어진다.

첫 줄에 노드 수 N(1≤N≤12)와 색상 번호 M(1≤M≤12)가 주어진다.

노드1부터의 칠해진 색상 번호 리스트를 출력한다.
불가능한 경우 -1을 출력한다.
'''
N, M = map(int, input().split())

maps = [[0 for x in range(N+1)]for y in range(N+1)]
color_list = [0] * (N+1)
result = -1
flag = 0

for y in range(1, N+1):
    colors = list(map(int, input().split()))
    for x in range(1, y):
        maps[y][x] = colors[x-1]
end = 0
def color(k=1):
    global color_list, result, flag, end
    if end == 1:
        return
    if k == N+1:
        result = ' '.join(map(str, color_list[1:]))
        end = 1
        return

    else:
        for i in range(1, M+1):
            flag = 0
            for j in range(1, k+1):
                color_list[k] = i
                if maps[k][j] == 1 and color_list[k] == color_list[j]:
                    flag = 1
                    break
            if flag != 1:
                color(k+1)
            if end == 1:
                return

color()
print(result)