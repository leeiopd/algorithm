'''
* DFS 순열 연습
N*N개의 수가 주어진다(1<=N<=10)
각행에서 수를 하나씩 뽑는다.
이 N개 수의 합을 구할때 최솟값을 구하시오.
단, 재귀함수로 구현한다.

* 단 2가지 방법으로 최소의 합을 찾는다.
1. 각행에서 수를 하나씩 뽑는다. 뽑은 N개 수의 합이 최소인 값을 구하시오.
2. 각행에서 수를 하나씩 뽑는다. 단 같은 열이 중복되지 않도록 뽑은 N개 수의 합이 최소인 값을 구하시오.

예로 입력값이 다음과 같다면 첫번째 방법으로 최소의 합이 되는 경우는 1+2+3=6이 된다.
두번째 방법으로 최소의 합이 되는 경우는 열이 겹치지 않도록 하여야 하므로 3+2+3=8이 된다.
1 5 3
2 4 7
5 3 5

'''

import sys

sys.stdin = open("6_input.txt")

N = int(input())
maps = []
for y in range(N):
    maps.append(list(map(int, input().split())))

visited = [-99] * N
top = -1
def game():
    global visited, ans2, top
    if top == N-1:
        add = 0
        for i in range(N):
            add += maps[i][visited[i]]
            if add > ans2:
                return
        if add < ans2:
            ans2 = add
            return
    add = 0
    for i in range(top):
        add += maps[i][visited[i]]
        if add > ans2:
            return

    for i in range(N):
        if i not in visited:
            top += 1
            visited[top] = i
            game()
            visited[top] = -99
            top -= 1


ans2 = 9999999999999999999

game()



ans1 = 0

for y in range(N):
    k = min(maps[y])
    ans1 += k

print(ans1)
print(ans2)